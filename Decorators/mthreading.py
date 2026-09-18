"""
Why multithreading is actually useful
The key idea is I/O bound work.- tasks where your program spends time waiting for some external.
. API response
. downloading files
. database queries
. reading from some external services.
. web request
so in threads while one thread is waiting for the network, another thread can make progress.
This is the main reason why we learning threading. 
"""
# import requests
# import time 

# def fetch_user(user_id):
#     url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
#     response = requests.get(url)
#     return response.json()

# start_time = time.perf_counter()
# print("Start Time", start_time)
# for user_id in range(1,6):
#     user = fetch_user(user_id)
#     # print(user)
#     # print("*"*150)

#     print(user["name"])
#     print()


# end_time = time.perf_counter()
# print("EndTime",end_time)
# print("*"*20)
# print('Time Taken', end_time - start_time)
# This was simple now use in threads

import requests
import threading
import time

def fetch_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    
    response = requests.get(url)
    # print(response.status_code)
    print(user_id)
    print(response.json()["name"])

start_time = time.perf_counter()

threads = []

for user_id in range(1, 6):
    # thread = threading.Thread(target=fetch_user, args=(user_id))
    thread = threading.Thread(target=fetch_user, args=(user_id,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.perf_counter()
print("Time Taken", end_time - start_time)