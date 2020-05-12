from flask import Flask, render_template, request, redirect
import csv

# configure app
app = Flask(__name__)


# welcome page
@app.route("/")
def home():
    return render_template("welcome.html")


# page to show tasks
@app.route("/tasks")
def tasks_todo():
    with open("tasks.csv", "r") as file:
        reader = csv.reader(file)
        tasks = list(reader)
    return render_template("show.html", tasks=tasks)


# page to show fail message
@app.route("/failure")
def failure():
    return render_template("failure.html")


# page to show to do list
@app.route("/todo", methods= ["POST"])
def register():
    task = request.form.get("task")
    date = request.form.get("date")
    importance = request.form.get("importance")

    #check if all info provided
    if not task or not date or not importance:
        return redirect("/failure")
    # using a csv as a database
    with open("tasks.csv", "a", newline="") as db:
        writer = csv.writer(db)
        # pass the values as a 3-valued tuple
        writer.writerow((task, date, importance))
    return redirect("/tasks")


if __name__ == "__main__":
    app.run(debug= True)