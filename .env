import os
from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import McpTool, ToolSet, ListSortOrder

# ------------------------------------------------------
# Load environment variables
# ------------------------------------------------------
load_dotenv()
PROJECT_ENDPOINT = "https://trainer-7457-resource.services.ai.azure.com/api/projects/trainer-7457"
MODEL_DEPLOYMENT ="gpt-4o-mini"  # Primary model for conversation

if not PROJECT_ENDPOINT or not MODEL_DEPLOYMENT:
    raise SystemExit("ERROR: Missing PROJECT_ENDPOINT or MODEL_DEPLOYMENT_NAME in .env")

# ------------------------------------------------------
# Create Azure Agents client
# ------------------------------------------------------
credential = DefaultAzureCredential(
    exclude_environment_credential=True,
    exclude_managed_identity_credential=True,
)

agents_client = AgentsClient(
    endpoint=PROJECT_ENDPOINT,
    credential=credential
)

# ------------------------------------------------------
# MCP Tool Setup
# ------------------------------------------------------
mcp_tool = McpTool(
    server_label="mslearn",
    server_url="https://learn.microsoft.com/api/mcp"
)
mcp_tool.set_approval_mode("never")

toolset = ToolSet()
toolset.add(mcp_tool)

# ------------------------------------------------------
# Prompt the user
# ------------------------------------------------------
user_prompt = input("\nHow can I help?: ")

# ------------------------------------------------------
# MAIN EXECUTION
# ------------------------------------------------------
with agents_client:

    print("\n--- Creating Agent ----------------------------------")

    try:
        agent = agents_client.create_agent(
            model=MODEL_DEPLOYMENT,
            name="my-mcp-agent",
            instructions="""
            You have access to an MCP server called `microsoft.docs.mcp`.
            Use it to search through official Microsoft documentation.
            """
        )
        print(f"✔ Agent created: {agent.id}\n")

    except Exception as e:
        print("\n❌ ERROR: Unable to create the agent.")
        print("This is usually caused by:")
        print(" - Wrong MODEL_DEPLOYMENT_NAME")
        print(" - Deployment not created in this AI Project")
        print("\nFull Azure error:")
        print(e)
        raise SystemExit("\nFix the deployment name and try again.")

    # --------------------------------------------------
    # Create thread
    # --------------------------------------------------
    thread = agents_client.threads.create()
    print(f"✔ Thread created: {thread.id}\n")

    # --------------------------------------------------
    # Add user message
    # --------------------------------------------------
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_prompt
    )
    print(f"✔ Message created: {message.id}\n")

    # --------------------------------------------------
    # Run the agent with tools
    # --------------------------------------------------
    print("--- Running agent with MCP tools --------------------\n")

    run = agents_client.runs.create_and_process(
        thread_id=thread.id,
        agent_id=agent.id,
        toolset=toolset
    )

    print(f"Run status: {run.status}")

    if run.status == "failed":
        print("\n❌ The agent run failed.")
        print("Azure error:", run.last_error)
        print("\nIf the error says:")
        print(" 'invalid_deployment' → You need a second model deployment (e.g., gpt-4o-mini).")
    else:
        print("✔ Run completed successfully.\n")

    # --------------------------------------------------
    # Print conversation
    # --------------------------------------------------
    print("\n--- Conversation -------------------------------------")
    messages = agents_client.messages.list(
        thread_id=thread.id,
        order=ListSortOrder.ASCENDING
    )

    for msg in messages:
        if msg.text_messages:
            content = msg.text_messages[-1].text.value
            print(f"{msg.role.upper()}: {content}")
            print("-" * 50)

    # --------------------------------------------------
    # Cleanup
    # --------------------------------------------------
    agents_client.delete_agent(agent.id)
    print("\n✔ Agent deleted.\n")

