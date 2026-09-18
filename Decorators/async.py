""""
Async programming is another way to handle task that takes times, especially
. Api request 
. network operation 
. database operation
. file I/O
. waiting for extenal service.

The key idea,while one task is waiting ,the program can work or another task instead of sitting idle.

aiohttp
A Python library for making HTTP requests asynchronously.
We used it because requests is synchronous/blocking.
We haven't actually studied aiohttp yet.

session / ClientSession
A ClientSession represents a reusable connection/session for communicating with a web server.
It can be reused for multiple HTTP requests instead of creating a new connection setup for every request.
We haven't discussed sessions yet.

async with
We already learned normal with and context managers.
async with is the asynchronous version of with.
But I should have explained how it differs before putting it into the API example.

asyncio.create_task()
We introduced asyncio.run() and asyncio.gather(), but I didn't properly teach create_task().
It schedules a coroutine to run as an asyncio Task.

asyncio.gather()
I used it before properly teaching it.
Its job is to wait for multiple async operations and collect their results.

await response.json()
We haven't discussed what an HTTP response is in async programming or why .json() itself needs await with aiohttp.
"""

# import asyncio
# import aiohttp


# async def fetch_user(session, user_id):
#     url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

#     async with session.get(url) as response:
#         user = await response.json()
#         return user


# async def main():
#     async with aiohttp.ClientSession() as session:

#         tasks = []

#         for user_id in range(1, 6):
#             task = asyncio.create_task(fetch_user(session, user_id))
#             tasks.append(task)

#         results = await asyncio.gather(*tasks)

#         for user in results:
#             print(user["id"], user["name"])


# asyncio.run(main())

import asyncio

async def task1():
    print("Task1 is started")
    await asyncio.sleep(2)
    print("Task1 is finished")

async def task2():
    print("Task2 is started")
    await asyncio.sleep(1)
    print("Task2 is finished")

async def main():
    task_one = asyncio.create_task(task1())
    
    task_two = asyncio.create_task(task2())

    print("Main is running")
    
    # await task_one
    # await task_two
    # instead of this use gather
    await asyncio.gather(task_one, task_two)

asyncio.run(main())