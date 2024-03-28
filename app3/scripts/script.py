from flask import Flask, request, render_template, jsonify
import jinja2
import requests




app = Flask(__name__, template_folder='/app')

@app.route('/submit_form', methods=['POST'])
def send_data():
    data = {
        'name': request.form['fname'],
        'age': request.form['age']
    }
    headers={'Content-Type': 'application/json'}
    response = requests.post('http://server1:5000/receive_data', json=data, headers=headers)
    return response.text

@app.route('/')
def home():
   return render_template('/html/index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)