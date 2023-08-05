## Minecraft Username Availability Checker

This Program checks the availability of Minecraft usernames using the Mojang API, managing retries, delays, and optional multithreading, and outputs the results into two separate text files.

### How to use

1. **Download the program**: Click on the `Checker.zip` file in the GitHub repository and then click the `Download` button. Once downloaded, extract the contents of the zip file to your desired location.

2. **Prepare the usernames**: Open the `usernames.txt` file that you extracted from the zip file. Add the Minecraft usernames that you want to check, one username per line, and save the file.

3. **Run the program**: Double-click on the `mc_username_checker.exe` file to run the program. The program will prompt you for the following inputs:
   - Number of retries for each username (0-10)
   - Delay (in seconds) between each retry (0-60)
   - Delay (in seconds) between each request (0-25)
   - Enable multithreading? (yes/no)
   - If multithreading is enabled, number of threads (1-50000)

4. **View the results**: After the program finishes running, you'll find two new text files in the same directory: `available.txt` contains the usernames that are available, and `in_use.txt` contains the usernames that are currently in use.

### Source Code

The `source_code.py` file in the GitHub repository contains the source code of the program. This is provided for educational purposes, for those who want to understand how the program works, or for those who wish to contribute to the project. You don't need to download this file to use the program.

### Notes

- The rate of requests and number of threads should be set carefully to avoid being blocked by the Mojang API for excessive requests.
- If the number of retries and delay between retries are set too high, the script could run for a long time if there are issues with the server or network.
- Multithreading can speed up the script but may increase the risk of hitting rate limits if not managed carefully.

### Disclaimer

This script is provided for educational purposes only. Always respect the terms of service of the API you are using.
