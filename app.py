from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hell_world():
	return render_template("home.html")

@app.route('/ask_question')
def ask_question():
	return render_template('ask_question.html')



if __name__ == '__main__':
	app.run(debug = True)
