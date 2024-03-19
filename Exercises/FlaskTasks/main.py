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
    return render_template('all_tasks.html', page_name='Tasks', list=task_list)

@app.route('/tasks/<task_id>')
def view_tasks_by_id(task_id):
    task = task_list[int(task_id)]
    return render_template('task.html', page_name='Task', task=task)


@app.route('/tasks/<task_id>/delete')
def delete_task_by_id(task_id):
    task_list.pop(int(task_id))
    return render_template('all_tasks.html', page_name='Tasks', list=task_list)

if __name__ == '__main__':
    app.run(debug=True)