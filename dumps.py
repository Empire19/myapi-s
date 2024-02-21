"""
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Initialize an empty list to store data
data = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

@app.route('/items', methods=['POST'])
def create_item():
    try:
        # Get JSON data from the request
        new_item = json.loads(request.data)
        data.append(new_item)
        return jsonify(new_item), 201
    except json.JSONDecodeError:
        return 'Invalid JSON data', 400

if __name__ == '__main__':
    app.run(debug=True)
"""


from flask import Flask,request,jsonify
import json


app = Flask(__name__)

data=[]

@app.route('/',methods=['GET','POST'])
def author():
    if request.method == 'GET':

        return jsonify(data)
    if request.method == "POST":
        try:
            new_dic=json.loads(request.data)
            data.append(new_dic)
            return jsonify(new_dic),201
        except json.JSONDecodeError:
            return 'invalid json data',400


if __name__ == '__main__':
    app.run(debug=True)

