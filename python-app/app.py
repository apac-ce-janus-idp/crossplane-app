from flask import Flask
import mysql.connector
import argparse

app = Flask(__name__)

@app.route('/')
def index():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--user", required=True, help="Database user")
        parser.add_argument("--password", required=True, help="Database password")
        parser.add_argument("--host", required=True, help="Database host")
        args = parser.parse_args()

        cnx = mysql.connector.connect(user=args.user, password=args.password, host=args.host)

        if cnx.is_connected():
            return 'connected'
        else:
            return 'not connected'
    except mysql.connector.Error as err:
        return f"Something went wrong: {err}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
