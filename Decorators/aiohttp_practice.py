"""
aiohttp is a library for making HTTP request asynchronously.
It is the async version of making request.

An async request is an HTTP request that doesn't block your program while waiting for the response. 
Your program can do other things while waiting for the server to reply.

async and await use to write code that can do multiple 
things at once without blocking, so our program doesnot freeze 
for slow task like api calls or file reads. 

async/await are the syntax(grammar) asyncio is the engine that makes that 
syntax to actually run. 

A session is a reusable connection object that keeps 
settings, cookies, and headers across multiple requests, 
so you don't have to set them up every time
"""

import asyncio
import aiohttp


async def fetch_user(session, user_id):
    try:
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        # url = "https://httpbin.org/delay/5"

        async with session.get(url) as response:
            response.raise_for_status()

            data = await response.json()

            return user_id, data["name"]
        
    except asyncio.TimeoutError:
        # print("Request Tiemout Error")
        return user_id, "Timeout"
    
    except aiohttp.ClientResponseError as e :
        if e.status  ==404:
            return user_id, "User not Found"
        
        return user_id, f"HTTP Error {e.status}"
        
    except aiohttp.ClientError:
        return user_id, "Connection Error"
    


async def main():
    time_out = aiohttp.ClientTimeout(total=3)

    async with aiohttp.ClientSession(timeout = time_out) as session:
        user_ids = [1, 2, 999]

        """
        This is creation of dynamic tasks. 
        Dynamic task creation means creating tasks while the program is running, 
        based on conditions, data, or user input — instead of writing them all out manually in advance.
        """
        tasks = [asyncio.create_task(fetch_user(session, user_id)) for user_id in user_ids ]

        results = await asyncio.gather(*tasks, return_exceptions=True)

        for result in results:
            if isinstance(result, Exception):

                """
                The main reason we're doing this is because gather(..., return_exceptions=True)
                gives us a mixture of successful results and exception objects in the same results list.
                And isinstance() lets us distinguish between those two.
                """
                print("Request failed:", result)
            else:
                user_id, name = result
                print(f"User {user_id}: {name}")


asyncio.run(main())