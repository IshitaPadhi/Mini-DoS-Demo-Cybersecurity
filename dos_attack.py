"""
=========================================================
Mini DoS Lab

dos_attack.py

Simulates a DoS attack by sending multiple HTTP requests
to a local server.

Author : Ishita Padhi
=========================================================
"""

# Import required libraries
import requests
import time

# URL of our local server
URL = "http://localhost:8000"

# Number of requests to send
TOTAL_REQUESTS = 500

# Counter for successful requests
successful_requests = 0

# Record attack start time
start_time = time.time()

print("=" * 50)
print("Mini DoS Attack Started")
print("=" * 50)

# Send multiple requests
for i in range(TOTAL_REQUESTS):

    try:

        # Send GET request
        response = requests.get(URL)

        # Check if request was successful
        if response.status_code == 200:

            successful_requests += 1

        # Print progress
        print(f"Request {i+1} Sent | Status : {response.status_code}")

    except Exception as e:

        print(f"Request {i+1} Failed")

# Record attack end time
end_time = time.time()

# Print summary
print("\n" + "=" * 50)
print("Attack Completed")
print("=" * 50)

print(f"Total Requests Sent : {TOTAL_REQUESTS}")
print(f"Successful Requests : {successful_requests}")
print(f"Failed Requests     : {TOTAL_REQUESTS-successful_requests}")
print(f"Time Taken          : {round(end_time-start_time,2)} seconds")