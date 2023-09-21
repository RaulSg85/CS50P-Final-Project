from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def redirect_home():
    return redirect("/video")

@app.route("/video")
def video():
    return render_template('video.html')

@app.route("/foto")
def foto():
    return render_template('foto.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)