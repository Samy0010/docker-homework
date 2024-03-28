from flask import Flask, request
import requests

app = Flask(__name__)

# Endpoint to send data via POST requests
@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.json  # Assuming JSON data is sent
    # Send data to Server 1
    response = requests.post('http://server1:5000/receive_data', json=data)
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

