# Print Statement
print ("Python With Flask")
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
return "Hello World!"
 
if __name__ == "__main__":
app.run()
	