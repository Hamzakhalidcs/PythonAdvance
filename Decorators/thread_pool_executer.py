"""
why ThreadPoolExecutor exists if manual Thread already gives us concurrency.

ThreadPoolExecutor doesn't fundamentally make the work more concurrent. 
It makes managing concurrent work easier, safer, and more scalable.

ThreadPoolExecutor isn't necessarily faster than manually created threads.
Your two timings already demonstrated that. 
Its main advantage is management, controlled concurrency, task scheduling, and easier result handling.
"""

import requests
import time 
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    
    response = requests.get(url)
    response.raise_for_status()
    # user = response.json()
    # return user
    # print(user_id, user["name"])
    return response.json()

# start_time = time.perf_counter()
futures  =[]

with ThreadPoolExecutor(max_workers=5) as executor:
    for user_id in range(1,6):
        future = executor.submit(fetch_user, user_id)
        # result = future.result()
        futures.append(future)

for future in as_completed(futures):
    
    try:
        result = future.result()
        print(result["id"], result["name"])
    
    except Exception as e :
        print("Task Failed", e)

# end_time = time.perf_counter()

# print("Time Taken", end_time - start_time)

