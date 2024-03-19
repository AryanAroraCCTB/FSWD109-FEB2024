from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo.db"
db = SQLAlchemy(app)


# Define User and Post models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    posts = db.relationship("Post", backref="author")

    def __str__(self):
        return f"User('{self.username}', '{self.email}')"

    def serialize(self, include_posts=True):
        if include_posts:
            return {
                "id": self.id,
                "username": self.username,
                "email": self.email,
                "posts": [post.serialize() for post in self.posts],
            }
        else:
            return {"id": self.id, "username": self.username, "email": self.email}


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)

    def __str__(self):
        return f"Post('{self.title}', '{self.content}', '{self.user_id}')"

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "user_id": self.user_id,
        }


@app.route("/", methods=["GET"])
def index():
    return jsonify(message=f"Welcome to FLASK DEMO WITH ORM"), 200


# -----------
# User ROUTES
# -----------
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


# -----------
# Post ROUTES
# -----------
@app.route("/posts", methods=["GET", "POST"])
def post():
    if request.method == "GET":
        return get_all_posts()
    elif request.method == "POST":
        return create_post(request.json)


@app.route("/posts/<post_id>", methods=["GET", "PUT", "DELETE"])
def post_by_id(post_id: int):
    id = int(post_id)
    if request.method == "GET":
        return get_post_by_id(id)
    elif request.method == "PUT":
        return update_post(id, request.json)
    elif request.method == "DELETE":
        return delete_post(id)


def get_all_posts():
    posts = Post.query.all()
    return (
        jsonify(message="Posts Found", data=[post.serialize() for post in posts]),
        200,
    )


def get_post_by_id(id):
    post = Post.query.get(id)
    if post is None:
        return jsonify(message=f"No Post with id {id}", data=None), 404
    return (
        jsonify(message="Posts Found", data=[post.serialize()]),
        200,
    )


def create_post(data):
    user = User.query.get(int(data["user_id"]))
    if user is None:
        return jsonify(message=f"No User with id {data["user_id"]}", data=None), 404
    
    new_post = Post(
        title=data["title"], content=data["content"], user_id=int(data["user_id"])
    )
    db.session.add(new_post)
    db.session.commit()
    return (
        jsonify(message="Post created successfully", data=new_post.serialize()),
        201,
    )


def update_post(id, data):
    post = Post.query.get(id)
    if post is None:
        return jsonify(message=f"No Post with id {id}", data=None), 404
    user = User.query.get(int(data["user_id"]))
    if user is None:
        return jsonify(message=f"No User with id {data["user_id"]}", data=None), 404
    post.title = data["title"]
    post.content = data["content"]
    post.user_id = int(data["user_id"])
    db.session.commit()
    return (
        jsonify(message="Post updated successfully", data=post.serialize()),
        200,
    )


def delete_post(id):
    post = Post.query.get(id)
    if post is None:
        return jsonify(message=f"No Post with id {id}", data=None), 404
    db.session.delete(post)
    db.session.commit()
    return jsonify(message="Post deleted successfully", data=None), 200


if __name__ == "__main__":
    # Ensure that we are working within the Flask application context
    with app.app_context():
        # Create database tables
        print(f"Creating Tables")
        db.create_all(force=True)
    app.run(debug=True)
