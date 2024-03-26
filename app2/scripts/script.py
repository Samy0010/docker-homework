# from flask import Flask, jsonify, request
# import time
# import sys
# import json

# sys.stdout.write("Output message\n")
# sys.stdout.flush()

# @app.route('/salut/<int:id>', methods=['GET'])
# def get_message(id):
#     message = next((message for message in messages if message['id'] == id), None)
#     if message:
#         return jsonify(message)
#     else:
#         return jsonify({"error": "message not found"}), 404

# while(True):
#     sys.stdout.write("salut\n")

#     try:
#         # Send the get request
#         response = request.get("http://server1:5000/salut")

#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             sys.stdout.write("Raise request submitted successfully!\n")
#             sys.stdout.write(json.dumps(response.json(), indent=2) + "\n")
#         else:
#             sys.stdout.write(f"Failed to submit raise request. Status code: {response.status_code}\n")
#     except Exception as e:
#         sys.stdout.write(f"Error occurred: {e}\n")
#     sys.stdout.flush()
#     time.sleep(10)

from flask import Flask, request
import requests

app = Flask(__name__)

# Endpoint to receive data via POST requests
@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.json  # Assuming JSON data is sent
    # Send data to Server B
    response = requests.post('http://server1:5000/receive_data', json=data)
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

