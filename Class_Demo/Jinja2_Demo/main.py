from flask import Flask, request, render_template

app = Flask(__name__)

users_list = [
    {
        "name": "def",
        "age": 25
    }, 
    {
        "name": "xyz",
        "age": 30
    },
    {
        "name": "abc",
        "age": 27
    }
]
books_list = [
    {
        "name": "book1",
        "year": 2025
    }, 
    {
        "name": "book2",
        "year": 2030
    },
    {
        "name": "book3",
        "year": 2027
    }
]

@app.route('/')
def index():
    return render_template('index.html', page_name='Home')

@app.route('/users')
def users():
    return render_template('users.html', page_name='Users', list=users_list)

@app.route('/books')
def books():
    return render_template('books.html', page_name='Books', list=books_list)

if __name__ == '__main__':
    app.run(debug=True)