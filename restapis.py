import requests
import httpx
import asyncio

# url = "https://jsonplaceholder.typicode.com/posts"

# params = {"id":10}

# response = requests.get(url, params=params)
# print ("Status code: ", response.status_code)
# print("Final URL ", response.url)

# posts = response.json()
# if response.status_code == 404:
#  #   print ("url not found")
#  pass
# else:
#     for post in posts:
#      #   print(post["body"])
#      pass
# #
# new_post = {
#     "userId": 1,
#     "title": "AMRIT TITLE",
#     "body": "Sample body by Amritansh Lal"
#   }

#response1 = requests.post(url, json=new_post)
# print(response1.status_code)
# print(response1.json())

async def fetch_post(post_id):
  url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
  async with httpx.AsyncClient() as client:
    response = await client.get(url)
    return response.json()

async def main():
  task=[fetch_post(i) for i in range(1,6)]
  result = await asyncio.gather(*task)

  for post in result:
    print("Post ID: ", post["id"], " | Title: ", post["title"])

asyncio.run(main())