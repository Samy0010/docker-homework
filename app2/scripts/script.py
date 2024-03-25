import requests
import time
import sys
import json

sys.stdout.write("Output message\n")
sys.stdout.flush()
while(True):
    sys.stdout.write("salut\n")

    try:
        # Send the POST request
        response = requests.get("http://server1:5000/salut")

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            sys.stdout.write("Raise request submitted successfully!\n")
            sys.stdout.write(json.dumps(response.json(), indent=2) + "\n")
        else:
            sys.stdout.write(f"Failed to submit raise request. Status code: {response.status_code}\n")
    except Exception as e:
        sys.stdout.write(f"Error occurred: {e}\n")
    sys.stdout.flush()
    time.sleep(10)

