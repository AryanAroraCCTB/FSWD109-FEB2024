from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo.db"
db = SQLAlchemy(app)


# Define User models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __str__(self):
        return f"User('{self.username}', '{self.email}')"

    def serialize(self):
        return {"id": self.id, "username": self.username, "email": self.email}


# ------
# ROUTES
# ------
@app.route("/", methods=["GET"])
def index():
    return f"Welcome to FLASK DEMO WITH ORM", 200


@app.route("/users", methods=["GET", "POST"])
def user():
    if request.method == "GET":
        return get_all_users()
    elif request.method == "POST":
        return create_user(request.json)


@app.route("/users/<user_id>", methods=["GET", "PUT", "DELETE"])
def user_by_id(user_id: int):
    id = int(user_id)
    if request.method == "GET":
        return get_user_by_id(id)
    elif request.method == "PUT":
        return update_user(id, request.json)
    elif request.method == "DELETE":
        return delete_user(id)


def get_all_users():
    users = User.query.all()
    return (
        jsonify(message="Users Found", data=[user.serialize() for user in users]),
        200,
    )


def get_user_by_id(id: int):
    user = User.query.get(id)
    if user is None:
        return jsonify(message=f"No User with id {id}", data=None), 404
    else:
        return jsonify(message="User Found", data=user.serialize()), 200


def create_user(data):
    new_user = User(username=data["username"], email=data["email"])
    db.session.add(new_user)
    db.session.commit()
    return (
        jsonify(message="User created successfully", data=new_user.serialize()),
        201,
    )


def update_user(id, data):
    user = User.query.get(id)
    if user is None:
        return jsonify(message=f"No User with id {id}", data=None), 404
    user.username = data["username"]
    user.email = data["email"]
    db.session.commit()
    return (
        jsonify(message="User updated successfully", data=user.serialize()),
        200,
    )


def delete_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify(message=f"No User with id {id}", data=None), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify(message="User deleted successfully", data=None), 200


if __name__ == "__main__":
    # Ensure that we are working within the Flask application context
    with app.app_context():
        # Create database tables
        print(f"Creating Tables")
        db.create_all()
    app.run(debug=True)
