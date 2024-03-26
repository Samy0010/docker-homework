from flask import Flask, jsonify, request, send_file
import json



# Sample data - you can replace this with your own data source
message = {"id": "0", "status": "success", "message": "Salut, aici server1!", "author": "Samy Abdulrahim"}

# Route to get all messages
# @app.route('/salut', methods=['GET'])
# def salut():
#     return jsonify(message)


    
# @app.route('/salut', methods=['POST'])
# def add_message():
#     new_message = request.json
#     message.append(new_message)
#     return jsonify({"message": "new message added"}), 201

app = Flask(__name__)

# Endpoint to receive POST requests from Server A
@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json
    # Add received data to a file
    with open('data.txt', 'a') as file:
        file.write(json.dumps(data) + '\n')
    return 'Data received successfully'

@app.route('/receive_data', methods=['GET'])
def get_data():
    # Assuming data is stored in data.txt
    with open('data.txt', 'r') as file:
        data = file.read()
    return data

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')

