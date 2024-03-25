from flask import Flask, jsonify

app = Flask(__name__)

# Sample data - you can replace this with your own data source
message = {"status": "success", "message": "Salut, aici server1!", "author": "Samy Abdulrahim"}

# Route to get all books
@app.route('/salut', methods=['GET'])
def salut():
    return jsonify(message)


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
