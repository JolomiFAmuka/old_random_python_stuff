
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)


@app.route("/")
def index():
    user_logged_in = False
    my_var = "Jolomi"
    letters = list(my_var)
    pup_dict = {"name":"sparky","breed":"chiuwawa"}
    puppies = ["Max", "Sparky", "Rufus", "Killa"]
    return render_template ('index.html', my_var = my_var, letters = letters, pup_dict = pup_dict, puppies = puppies, user_logged_in = user_logged_in)

@app.route("/information")
def info():
    return "<h1>This is the information center</h1>"

@app.route("/user/<name>")
def user(name):
    return f"<h1>Username: {name}</h1>"

if __name__ == '__main__':
    app.run(debug=True)