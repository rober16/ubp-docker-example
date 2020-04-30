from flask import Flask
from flask import jsonify
import mysql.connector
import os
app = Flask(__name__)


def get_connection():
    """
    This function connect with db on http://db host (dockerized)
    Needs DB_USER_NAME and DB_PASSWORD
    :return: DB connection
    """
    config = {
        'user': os.environ.get('DB_USER_NAME','root'),
        'password': os.environ.get('DB_PASSWORD','root'),
        'host': 'db',
        'port': '3306',
        'database': 'drinks'
    }
    connection = mysql.connector.connect(**config)
    return connection

@app.route('/')
def index():
    """
    Web's homepage
    :return: HTTP response
    """
    hello = os.environ.get('NAME_HELLO',None)
    if not hello:
        hello='Tu variable de entorno "NAME_HELLO" no se cargo correctamente'
    else:
        hello = 'Hola {}'.format(hello)
    return u'{}'.format(hello)

@app.route('/wines/')
def wines():
    """
    'API' endpoint for wines
    :return: HTTP response
    """
    connection=get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * From wines')
    wines = [{'name':name, 'color':color } for (name,color) in cursor]
    cursor.close()
    connection.close()
    return jsonify({'wines':wines})

if __name__ == '__main__':
    app.run(host='0.0.0.0')