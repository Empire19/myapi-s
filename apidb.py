'''
from flask import Flask, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key='637465'

# Database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Dharun@0501'
app.config['MYSQL_DB'] = 'mini'
mysql = MySQL(app)

# Create a MySQL database connection

@app.route('/fetch', methods=['GET'])
def fetch_data():
    try:
        # Execute the SQL query to select data from the 'apidata' table
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM WHERE apidata id = %s AND name = %s",(id,name))
        result = cursor.fetchall()
        mysql.connection.commit()
        cursor.close()


        # Convert the result to a list of dictionaries
        data_list = []
        for row in result:
            data_dict = {
                'id': row[0],
                'name': row[1]
                # Add more columns as needed
            }
            data_list.append(data_dict)

        return jsonify(data_list)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
'''

from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = '637465'

# Database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Dharun@0501'
app.config['MYSQL_DB'] = 'mini'
mysql = MySQL(app)

# Create a MySQL database connection

@app.route('/fetch', methods=['GET'])
def fetch_data():
    try:
        # Get 'id' and 'name' from the URL parameters
        id = request.args.get('id')
        name = request.args.get('name')

        # Execute the SQL query to select data from the 'apidata' table
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM apidata WHERE id = %s AND name = %s", (id, name))
        result = cursor.fetchall()
        mysql.connection.commit()
        cursor.close()

        # Convert the result to a list of dictionaries
        data_list = []
        for row in result:
            data_dict = {
                'id': row[0],
                'name': row[1]
                # Add more columns as needed
            }
            data_list.append(data_dict)

        return jsonify(data_list)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
