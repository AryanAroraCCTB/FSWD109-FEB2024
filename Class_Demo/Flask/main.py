from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/task/<int:task_id>')
def view_task(task_id):
    task = tasks[task_id]
    return render_template('task.html', task=task, task_id=task_id)

@app.route('/new_task', methods=['GET', 'POST'])
def new_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        tasks.append({'title': title, 'description': description})
        return redirect(url_for('index'))
    return render_template('new_task.html')

@app.route('/update_task/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        tasks[task_id] = {'title': title, 'description': description}
        return redirect(url_for('index'))
    return render_template('update_task.html', task=tasks[task_id], task_id=task_id)

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    del tasks[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
