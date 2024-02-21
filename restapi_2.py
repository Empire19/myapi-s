from flask import Flask
from flask_cors  import  CORS,cross_origin
from flaskext.mysql import  MySQL
import pymysql
from flask import jsonify
import json
from flask import request


app = Flask(__name__)
CORS(app)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Dharun@0501'
app.config['MYSQL_DATABASE_DB'] = 'mini'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

'''

CREATE TABLE clg (
    cname VARCHAR(250) NOT NULL,
    carea VARCHAR(250) NOT NULL,
    ctypes VARCHAR(250) NOT NULL,
    cemailid VARCHAR(250) NOT NULL,
    ctier VARCHAR(10) NOT NULL,
    cyear VARCHAR(10) NOT NULL,
    ccourse varchar(250),
    cid int (10) not null primary key auto_increment
);
'''

@app.route('/clg',methods=['POST'])

def create():
    conn = None
    cursor= None


    try:
        college_data=request.json
        cname = college_data['cname']
        carea=college_data['carea']
        ctypes=college_data['ctypes']
        cemailid = college_data['cemailid']
        ctier = college_data['ctier']
        cyear = college_data['cyear']
        ccourse = college_data['ccourse']

        if cname and carea and ctypes and cemailid and  ctier and cyear and ccourse and  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO clg (cname,carea,ctypes,cemailid,ctier,cyear,ccourse) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            bindata =(cname,carea,ctypes,cemailid,ctier,cyear,ccourse)
            cursor.execute(sqlQuery,bindata)
            conn.commit()
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



@app.route('/clg1', methods=['GET'])
def get():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT cname,carea,ctypes,cemailid,ctier,cyear,ccourse,cid FROM clg")
        clg=cursor.fetchall()
        respone = jsonify(clg)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/clgup/<int:id>', methods=['PUT'])
def update_emp(cid):
    conn = None
    cursor = None

    try:
        # Ensure that the request content type is 'application/json'
        if request.headers['Content-Type'] == 'application/json':
            # Parse JSON data from the request body
            college_data= request.get_json()
            cname = college_data['cname']
            carea= college_data['carea']
            ctypes= college_data['ctypes']
            cemailid = college_data['cemailid']
            ctier = college_data['ctier']
            cyear= college_data['cyear']
            ccourse = college_data['ccourse']

            if cname and carea and ctypes and cemailid and ctier and cyear and ccourse and cid and request.method == 'PUT':
                sqlQuery = "UPDATE clg SET cname=%s,carea=%s,ctypes=%s,cemailid=%s,ctier=%s,cyear=%s,ccourse=%s WHERE cid=%s"
                bindData = (cname,carea,ctypes,cemailid,ctier,cyear,ccourse,cid,)
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
           return jsonify({'error': 'Invalid Content-Type. Use application/json.'}), 400
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()



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
