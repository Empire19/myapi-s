from flask import Flask, request, jsonify
from flaskext.mysql import MySQL
import pymysql
import re

app = Flask(__name__)


mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Dharun@0501'
app.config['MYSQL_DATABASE_DB'] = 'mini'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

'''
# Create a table to store user information
def create_user_table():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

create_user_table()

# Function to check if a username meets complexity requirements
def is_valid_username(username):
    # Add your username complexity rules here (e.g., minimum length, character types)
    if len(username) >= 8:
        return True
    return False

# Function to check if a password meets complexity requirements
def is_valid_password(password):
    # Add your password complexity rules here (e.g., minimum length, special symbols)
    if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        return True
    return False

# Registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if not is_valid_username(username):
        return jsonify({'message': 'Invalid username'}), 400

    if not is_valid_password(password):
        return jsonify({'message': 'Invalid password'}), 400

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO login (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Registration successful'})

'''

username_pattern = r"^[a-zA-Z0-9_]{8,}$"
password_pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Function to check if a username meets complexity requirements using regex
def valid_username(username):
    return bool(re.match(username_pattern, username))

# Function to check if a password meets complexity requirements using regex
def valid_password(password):
    return bool(re.match(password_pattern, password))

def  valid_email(email):
    return bool(re.match(email_pattern,email))

# Registration route
@app.route('/reg', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    email = data['email']

    if not valid_username(username):
        return jsonify({'message': 'Invalid username'}), 400

    if not valid_password(password):
        return jsonify({'message': 'Invalid password'}), 400

    if not valid_email(email):
        return jsonify({'message': 'email'}), 400

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO login (username, password,email) VALUES (%s, %s,%s)", (username, password,email))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Registration successful'})



@app.route('/get',methods=['GET'])

def show():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id,username,password,email FROM login")
        user = cursor.fetchall()
        respone = jsonify(user)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

'''
# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM login WHERE username = %s", username)
    user = cursor.fetchone()
    conn.close()

    if user and user['password'] == password:
        return jsonify({'message': 'Login successful'})
    return jsonify({'message': 'Incorrect username or password'}), 401
'''


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
