from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics
import urllib.request
import json

app = Flask(__name__)
metrics = PrometheusMetrics(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

@app.route('/add', methods=["POST"])
def add():
    data = request.form["todo_item"]
    todo = Todo(text=data, complete=False)
    db.session.add(todo)
    db.session.commit()
    # return data # DEBUG REQUEST
    return redirect(url_for("index")) 


@app.route('/update', methods=["POST"])
def update():
    # return request.form # DEBUG REQUEST
    return redirect(url_for("index"))

data = json.load(urllib.request.urlopen("http://api.open-notify.org/iss-now.json"))
open_notify= metrics.info('API_open_notify','Текущее местоположение Международной космической станции', latitude=data['iss_position']['latitude'],longitude=data['iss_position']['longitude'])
open_notify.set(data['timestamp'])

if __name__ == '__main__':
    app.run(debug=True)