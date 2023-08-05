## Minecraft Username Availability Checker

This Python script checks the availability of Minecraft usernames using the Mojang API. It reads a list of usernames from a text file, sends requests to the Mojang API to check the availability of each username, and writes the results to two separate text files.

### Features

- Read list of usernames from a text file
- Check username availability using Mojang API
- Write available and in-use usernames to separate text files
- Configurable number of retries per username
- Configurable delay between retries and requests
- Option to enable multithreading with configurable number of threads

### Usage

1. Prepare a text file named `usernames.txt` with the list of usernames to check, one username per line.
2. Run the script: `python mc_username_checker.py`
3. The script will prompt you for the following inputs:
   - Number of retries for each username (0-10)
   - Delay (in seconds) between each retry (0-60)
   - Delay (in seconds) between each request (0-25)
   - Enable multithreading? (yes/no)
   - If multithreading is enabled, number of threads (1-50000)
4. The script will check the availability of each username and write the results to `available.txt` and `in_use.txt`.

### Requirements

- Python 3.6+
- `requests` library

### Notes

- The rate of requests and number of threads should be set carefully to avoid being blocked by the Mojang API for excessive requests.
- If the number of retries and delay between retries are set too high, the script could run for a long time if there are issues with the server or network.
- Multithreading can speed up the script but may increase the risk of hitting rate limits if not managed carefully.

### Disclaimer

This script is provided for educational purposes only. Always respect the terms of service of the API you are using.
