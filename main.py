from flask import Flask, render_template
import os

#  export FLASK_ENV=development
# Use flask run with 

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

todo_list = ["Default item", "test item"]

@app.route("/")
def index():
    cwd = os.getcwd()
    print(cwd)
    return render_template("index.html")

@app.route("/todo")
def todo():
    return render_template("todo.html", todo_list=todo_list)

@app.route("/finance")
def finance():
    return render_template("finance.html", a = [1,2,3])

if __name__ == "__main__":
    app.run()