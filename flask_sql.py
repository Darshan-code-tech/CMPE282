from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists

app = Flask(__name__)

app.config['SECRET_KEY'] = "jasdnlasndlnasd"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/admin"
db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return jsonify({
            "result": True,
            "message": "works"
        })
    elif request.method == "POST":
        input = request.get_json()
        emp_obj = Employee(name=input["name"])
        db.session.add(emp_obj)
        db.session.commit()
        return jsonify({
            "result": True,
            "message": "employee added to database"
        })

@app.route('/get-all-users')
def get_user():
    emp_obj = Employee.query.all()
    res = []
    for i in emp_obj:
        res.append(i.name)

    return jsonify({
        "result": True,
        "data": res
    })



if __name__ == "__main__":
    db_uri = "postgresql://postgres:postgres@localhost/admin"
    if not database_exists(db_uri):
        create_database(db_uri)

    db.create_all()
    app.run(debug=True, use_reloader=True)