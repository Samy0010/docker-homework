from flask import Flask, request, render_template, jsonify
import jinja2
import requests




app = Flask(__name__, template_folder='/app')

# Endpoint to receive data via POST requests
@app.route('/submit_form', methods=['POST'])
def send_data():
    data = {
        'name': request.form['fname'],
        'age': request.form['age']
    }
    headers={'Content-Type': 'application/json'}
    # Send data to Server 1
    response = requests.post('http://server1:5000/receive_data', json=data, headers=headers)
    return response.text
# html
@app.route('/')
def home():
   return render_template('/html/index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)