from flask import Flask, request, render_template

app = Flask(__name__)

task_list = [
    { 'name': 't1', 'date': 2020 },
    { 'name': 't2', 'date': 2021 },
    { 'name': 't3', 'date': 2022 }
]

@app.route('/')
def index():
    return render_template('index.html', page_name='Home')

@app.route('/tasks')
def view_tasks():
    return render_template('tasks.html', page_name='Task', list=task_list)

@app.route('/tasks/<task_id>')
def view_tasks_by_id(task_id):
    return render_template('tasks.html', page_name='Task', list=task_list)

if __name__ == '__main__':
    app.run(debug=True)