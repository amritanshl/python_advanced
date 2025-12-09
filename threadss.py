# import threading
# def task():
#     print("Thread is running")

# ti = threading.Thread(target=task)
# ti.start()
# ti.join()

# from multiprocessing import Process

# def task2():
#     print("process running")
# p = Process(target=task2)
# p.start()

# p.join()

import asyncio
import aiohttp

# async def task(name):
#     print(f"{name} started")
#     await asyncio.sleep(10)
#     print(f"{name} ended")
# async def main():
#     await asyncio.gather(
#         task("Amrit"),
#         task("Varun"),
#         task("debu"),
#         task("Sushma")
#     )
# asyncio.run(main())

# async def fetch_data(name, delay):
#     print(f"Downloading....{name}")
#     await asyncio.sleep(delay)
#     print(f"Done with downloading {name}")
    

# async def main():
#    await asyncio.gather(
       
#        fetch_data("amrit.txt",4),
#        fetch_data("mahi.csv", 10),
#        fetch_data("varun.log", 2),
#        fetch_data("kareena.sql", 15)
#    )
# asyncio.run(main())
async def  fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url}: {response.status}")
async def main():
    urls = ["https://httpbin.org/"]
    await asyncio.gather(*(fetch(url) for url in urls))
asyncio.run(main())