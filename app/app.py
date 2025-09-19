from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    db_host = os.environ.get("DB_HOST", "db")
    db_user = os.environ.get("DB_USER", "root")
    db_pass = os.environ.get("DB_PASS", "secret")
    db_name = os.environ.get("DB_NAME", "mydb")

    try:
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name
        )
        return "Flask connected to MySQL successfully!"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
