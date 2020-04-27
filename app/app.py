from flask import Flask
import mysql.connector
import json
from flask import jsonify

app = Flask(__name__)


def get_connection():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'drinks'
    }
    connection = mysql.connector.connect(**config)
    return connection

@app.route('/')
def index():
    return u'HOLASSS!!!!!!'


@app.route('/wines/')
def wines():
    connection=get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * From wines')
    wines = [{'name':name, 'color':color } for (name,color) in cursor]
    cursor.close()
    connection.close()
    return jsonify({'wines':wines})
    # return json.dumps({'wines':wines})

if __name__ == '__main__':
    app.run(host='0.0.0.0')