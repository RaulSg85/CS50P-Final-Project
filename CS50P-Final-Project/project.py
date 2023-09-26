from flask import Flask, render_template, redirect
import os


app = Flask(__name__)

@app.route("/")
def redirect_home():
    return redirect("/video")

@app.route("/video")
def video():
    list = get_list_of_filenames("Video")
    return render_template('video.html', list = list)

@app.route("/foto")
def foto():
    list = get_list_of_filenames("Foto")
    return render_template('foto.html', list = list )

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

def get_list_of_filenames(directory):
    dir_path = r'static/' + directory
    

    list = []

    for file in os.listdir(dir_path):
        list.append(file)

    return list

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)