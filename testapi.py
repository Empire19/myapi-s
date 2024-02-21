from flask import Flask, jsonify, request

app = Flask(__name__)
emp = [
    {"name": "sanjay",
     "age": 21,
     "role": "developer"},
{"name": "kishore",
     "age": 21,
     "role": "developer"},
{"name": "siva",
     "age": 23,
     "role": "developer"}
]

@app.route("/", methods=["GET"])
def get():
    if request.method=='GET':
        return jsonify(emp)
    else:
        return "No data available."

@app.route("/", methods=["POST"])
def post():
    if request.method == "POST":
        req_json = request.json
        new_emp = {
            'name': req_json['name'],
            'age': req_json['age'],
            'role': req_json['role']
        }
        emp.append(new_emp)
        return jsonify(new_emp)


@app.route("/<string:name>", methods=["PUT"])
def put(name):
    for e in emp:
        if e['name'] == name:
            req_json = request.json
            e['name'] = req_json['name']
            e['age'] = req_json['age']
            e['role'] = req_json['role']
            return jsonify(e), 200
    return "Employee not found.", 404



@app.route("/<string:name>", methods=["DELETE"])
def delete(name):
    for e in emp:
        if e['name'] == name:
            emp.remove(e)
            return jsonify({"message": "Employee deleted."}), 200
    return "Employee not found.", 404


if __name__ == "__main__":
    app.run(debug=True)
