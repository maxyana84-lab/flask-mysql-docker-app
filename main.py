import os
import time
from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    # Try to connect up to 10 times if the database is still initializing
    for i in range(10):
        try:
            conn = mysql.connector.connect(
                host=os.getenv('MYSQL_HOST', 'db'),
                port=int(os.getenv('MYSQL_PORT', 3306)),
                database=os.getenv('MYSQL_DB', 'your_db_name'),
                user=os.getenv('MYSQL_USER', 'your_db_user'),
                password=os.getenv('MYSQL_PASSWORD', 'your_db_password')
            )
            return conn
        except mysql.connector.Error:
            time.sleep(3)
    raise Exception("Could not connect to the database")

@app.route('/')
def index():
    try:
        mysql_conn = get_db_connection()
        cursor = mysql_conn.cursor()
        
        # Increment the page view counter
        cursor.execute("UPDATE page_counter SET count = count + 1")
        mysql_conn.commit()
        
        # Fetch the current counter value
        cursor.execute("SELECT count FROM page_counter")
        result = cursor.fetchone()
        
        count = result[0] if result else 0
        
        cursor.close()
        mysql_conn.close()
        
        return f"<h1>Hello World! This page has been viewed {count} times.</h1>"
    except Exception as e:
        return f"<h1>Internal Server Error</h1><p>{str(e)}</p>", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
