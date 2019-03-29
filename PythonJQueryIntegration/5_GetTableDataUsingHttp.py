# Hello World Program using Flask
print ("Python With Flask")

import drda
from flask import Flask

# __name__ means this current file. In this case, it will be PythonWithFlask.py. 
# This current file will represent my web application

# We are creating an instance of the Flask class and calling it app. 
# Here we are creating a new web application
app = Flask(__name__)

@app.route('/getData')	
def hello():
    conn = drda.connect(host='localhost', database='db', port=1527)
    cur = conn.cursor()
    cur.execute('select * from test')
    strValue = ''
    for r in cur.fetchall():
        strValue = strValue + ' ' + str(r[0])
    print(strValue)  
    return strValue
 
# When you run your Python script, Python assigns the name “__main__” to the script when executed
if __name__ == "__main__":
    app.run(debug='true')
	