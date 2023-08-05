import requests
import time
import threading
import queue

print("""
 .----------------.  .----------------. 
| .--------------. || .--------------. |
| | ____    ____ | || |     ______   | |
| ||_   \  /   _|| || |   .' ___  |  | |
| |  |   \/   |  | || |  / .'   \_|  | |
| |  | |\  /| |  | || |  | |         | |
| | _| |_\/_| |_ | || |  \ `.___.'\  | |
| ||_____||_____|| || |   `._____.'  | |
| |              | || |              | |
| '--------------' || '--------------' |
 '----------------'  '----------------' 
                                                   
This script will take a list of Minecraft usernames from 'usernames.txt', 
check their availability using the Mojang API, and output two files: 
'available.txt' with available usernames and 'in_use.txt' with usernames 
currently in use. You can set the number of retries, delay between retries, 
delay between requests, and number of threads for multithreading.
""")

def validate_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
            elif max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def worker(q, retries, retry_delay, available, in_use):
    while not q.empty():
        username = q.get()
        URL = f"https://api.mojang.com/users/profiles/minecraft/{username}"
        for _ in range(retries):
            response = requests.get(URL)
            if response.status_code == 200:
                in_use.append(username)  # Username is in use
                break
            elif response.status_code in [204, 404]:
                available.append(username)  # Username is available
                break
            elif response.status_code == 429:
                print("Rate limit exceeded. Waiting before retrying...")
                time.sleep(retry_delay)
            else:
                time.sleep(retry_delay)  # Wait for a specified delay before the next retry
        q.task_done()

def main(retries, retry_delay, request_delay, num_threads):
    with open('usernames.txt', 'r') as file:
        usernames = file.read().splitlines()

    available = []
    in_use = []

    q = queue.Queue()
    for username in usernames:
        q.put(username)

    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(q, retries, retry_delay, available, in_use))
        t.start()

    q.join()  # Block until all tasks are done

    with open('available.txt', 'w') as file:
        file.write('\n'.join(available))

    with open('in_use.txt', 'w') as file:
        file.write('\n'.join(in_use))

if __name__ == "__main__":
    retries = validate_input("Enter the number of retries for each username: ", min_value=0, max_value=10)
    retry_delay = validate_input("Enter the delay (in seconds) between each retry: ", min_value=0, max_value=60)
    request_delay = validate_input("Enter the delay (in seconds) between each request: ", min_value=0, max_value=25)
    multithreading = input("Do you want to enable multithreading? (yes/no): ").lower()
    if multithreading in ['yes', 'y']:
        num_threads = validate_input("Enter the number of threads: ", min_value=1, max_value=50000)
    else:
        num_threads = 1
    main(retries, retry_delay, request_delay, num_threads)