from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    def __str__(self):
        return f"{self.username} - {self.email}"


@app.route("/", methods=["GET"])
def index():
    return "Hello"


@app.route("/get_all_user", methods=["GET"])
def get_all_user():
    users = User.query.all()
    print(f"{users[0]}")
    return ""


@app.route("/get_user_by_name/", methods=["GET"])
def get_user_by_name():
    name = "xyz"
    user = User.query.filter(User.username == name).all()
    print(f"{user}")
    return f"{user}"


@app.route("/get_user_by_id/<id>", methods=["GET"])
def get_user_by_id(id):
    user = User.query.get(int(id))
    print(f"{user}")
    return f"{user}"


@app.route("/add_user", methods=["GET"])
def add_new_user():
    new_user = User(username="abc", email="abc@gmail.com")
    db.session.add(new_user)
    db.session.commit()
    return f"Adding new User: {new_user}"


@app.route("/update_user/<id>", methods=["GET"])
def update_user(id):
    user = User.query.get(int(id))
    user.username = "xyz_new"
    db.session.commit()
    return f"Updating User: {user}"


@app.route("/delete_user/<id>", methods=["GET"])
def delete_user(id):
    user = User.query.get(int(id))
    db.session.delete(user)
    db.session.commit()
    return f"Deleted User: {user}"


if __name__ == "__main__":
    with app.app_context():
        # Create database tables
        print(f"Creating Tables")
        db.create_all()
    app.run(debug=True)
