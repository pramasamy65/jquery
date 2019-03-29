
# Here we are importing the Flask module and creating a Flask web server from the Flask module
from flask import Flask, render_template

# __name__ means this current file. In this case, it will be PythonWithFlask.py. 
# This current file will represent my web application

# We are creating an instance of the Flask class and calling it app. 
# Here we are creating a new web application
app = Flask(__name__)

@app.route('/greet')
def hello():
    return 'Hello World!'

@app.route('/')
def indexPage():
    return render_template('index.html')
 
# When you run your Python script, Python assigns the name “__main__” to the script when executed
if __name__ == "__main__":
    app.run()
	