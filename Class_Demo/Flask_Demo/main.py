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

@app.route('/', methods=['GET'])
def home(): # view function
    print(f'Request Object: {request.method}')
    return render_template('index.html')

@app.route('/users', methods=['GET', 'POST'])
def users():
    print(f'Request Object: {request.method} {request.args}')
    if request.method == 'GET':
        age_limit = int(request.args.get('age_limit'))
        if age_limit:
            filtered_users_list = []
            
            for user in users_list:
                if user["age"] >= age_limit:
                    filtered_users_list.append(user)
            
            return filtered_users_list

        return users_list
    
    if request.method == 'POST':
        new_user = request.json
        users_list.append(new_user)

        return f'New user {new_user["name"]} added!'

@app.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_by_id(user_id):
    if request.method == 'GET':
        return users_list[int(user_id)]
    
    if request.method == 'PUT':
        new_user_data = request.json
        users_list[int(user_id)] = new_user_data
        return users_list[int(user_id)]
    
    if request.method == 'DELETE':
        deleted_user = users_list.pop(int(user_id))
        return f'Deleted user with name {deleted_user["name"]}'

if __name__ == '__main__':
    app.run(debug=True)
