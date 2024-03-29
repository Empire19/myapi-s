#app.py
from flask import  Flask
from flask_cors import CORS,cross_origin

#config .py
from flaskext.mysql import MySQL

#main.py
import  pymysql
from flask import jsonify
import  json
from flask import flash,request


app = Flask(__name__)
CORS(app)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Dharun@0501'
app.config['MYSQL_DATABASE_DB'] = 'mini'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

'''
json_data = {}

headers ={
  "content-Type": "application/json"
}
'''

#CREATE
@app.route('/create', methods=['POST'])
def create():
    conn = None
    cursor = None

    try:
        json_data= request.json
        name =  json_data['name']
        email =  json_data['email']
        phone =  json_data['phone']
        address = json_data['address']

        if name and email and phone and address and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO crud (name, email ,phone, address) VALUES (%s, %s, %s, %s)"
            binData = (name, email, phone, address)
            cursor.execute(sqlQuery, binData)
            conn.commit()
        #    json_data = json.dumps(json_data)

            response = jsonify({'message': 'Added Successfully'})
            return response
        else:
            return showmessage()
    except Exception as e:
        print(e)
        return jsonify({'error': 'An error occurred'}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

#GET METHOD
@app.route('/emp', methods=['GET'])
def show():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id,name,email,phone,address FROM crud")
        crud=cursor.fetchall()
        respone = jsonify(crud)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# show one by one
@app.route('/emp/<int:id>',methods=['GET'])
def onebyone(id):
    conn = None
    cursor = None

    try:
        conn=mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id,name,email,phone,address FROM crud WHERE id=%s",id)
        crud=cursor.fetchone()
        respone = jsonify(crud)
        respone.status_code=200
        return respone
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
'''
@app.route('/update/<int:id>', methods=['PUT'])
def update_emp(id):
    conn = None
    cursor = None

    try:
        json_data = request.json
        id = json_data['id']
        name = json_data['name']
        email = json_data['email']
        phone = json_data['phone']
        address = json_data['address']
        if name and email and phone and address and id and request.method == 'PUT':
            sqlQuery = "UPDATE crud SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
            bindData = (name, email, phone, address, id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Employee updated successfully!')
            respone.status_code = 200
            return respone
        else:
           return showmessage()
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

'''
#UPDATE
@app.route('/update/<int:id>', methods=['PUT'])
def update_emp(id):
    conn = None
    cursor = None

    try:
        # Ensure that the request content type is 'application/json'
        if request.headers['Content-Type'] == 'application/json':
            # Parse JSON data from the request body
            json_data = request.get_json()
            name = json_data['name']
            email = json_data['email']
            phone = json_data['phone']
            address = json_data['address']

            if name and email and phone and address and id and request.method == 'PUT':
                sqlQuery = "UPDATE crud SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
                bindData = (name, email, phone, address, id,)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sqlQuery, bindData)
                conn.commit()
                response = jsonify({'message': 'Employee updated successfully!'})
                response.status_code = 200
                return response
            else:
                return showmessage()
        else:
            # If Content-Type is not 'application/json', return an error response
            return jsonify({'error': 'Invalid Content-Type. Use application/json.'}), 400
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

#DELETE
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_emp(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM crud WHERE id =%s", (id))
		conn.commit()
		respone = jsonify('Employee deleted successfully!')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

#ERROR MSG
@app.errorhandler(404)
def showmessage(error=None):
    message={
        'status': 404,
        'message': 'Record not found:'+ request.url,

    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True)



