from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    try:
        cnx = mysql.connector.connect(user='admin', password='password',
                                      host='<rds-endpoint>'
                                    )
        if cnx.is_connected():
            return 'connected'
        else:
            return 'not connected'
    except mysql.connector.Error as err:
        return f"Something went wrong: {err}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)