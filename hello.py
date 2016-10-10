from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Index Page!"

@app.route("/name")
def name():
	return "Your name is:"

@app.route("/name/<jamie>")
def name_two(jamie):
	return "Your name is:" + jamie

if __name__ == "__main__":
	app.run()
