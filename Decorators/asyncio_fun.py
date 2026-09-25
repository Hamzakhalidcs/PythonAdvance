"""
Async is a Python keyword used to define asynchronous functions. 
Async is used to write code that can do multiple thiing at once without 
waiting for one task to finish before another task started.
Asycnion is a library/module in Python.
Asyncio ia a built-in python module that provides the tools to run and manage 
asynchronous code. 

await tells Python:
 "Pause here and wait for this task to finish, but while waiting, let other tasks run."
"""

import asyncio

async def divided(a, b):
    await asyncio.sleep(1)
    return a/b

async def main():
    try:
        result = await divided(10, 0)
        print(result)

    except ZeroDivisionError as e :
        print("Error", e)

asyncio.run(main())
