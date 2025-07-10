from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		print("Form submitted successfully!")
		print("Form Data:", request.form)
		return "Registration successful!"
	return render_template('register.html')
if __name__ == '__main__':
	app.run(debug=True)