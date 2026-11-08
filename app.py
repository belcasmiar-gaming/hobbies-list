from flask import Flask, render_template

app = Flask(__name__)

hobbies = [
    "Swimming",
    "Gaming",
    "Kayaking",
    "Watching TV",
    "Building Lego sets",
]


@app.route("/")
def home():
    return render_template("home.html", hobbies=hobbies)


@app.route("/tasks")
def tasks():
    return render_template("tasks.html", hobbies=hobbies)


if __name__ == "__main__":
    app.run(debug=True)