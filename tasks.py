from flask import Flask, redirect, render_template, request, url_for
from sqlalchemy import select

from app.database_config import DBSession, Tasks

app = Flask(__name__, template_folder="templates", static_url_path='/static')

session = DBSession()
tasks = []
@app.route('/')
def index():
    session = DBSession()
    with session as session:
        query = select(Tasks)
        tasks = session.execute(query).scalars().unique().all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/add', methods= ['POST', 'GET'])
def add():
    tasks = []
    if request.method == 'POST':
        session = DBSession()
        task = request.form['task']
        with session as session:
            new_task = Tasks(name=task)
            session.add(new_task)
            session.commit()
            tasks = get_tasks(session=session)
    return render_template("tasks.html", tasks=tasks)


def get_tasks(session):
    with session as session:
        query = select(Tasks)
        tasks = session.execute(query).scalars().unique().all()
    return tasks


@app.route("/open", methods=['POST', 'GET'])
def open():
    session = DBSession()
    if 'open' in request.form:
        task_id = request.form['open']
        with session as session:
            query = select(Tasks).filter(Tasks.id == task_id)
            task = session.execute(query).scalars().unique().one()
            tasks = get_tasks(session=session)
        return render_template("tasks_counter.html", counter="25:00", tasks=tasks, task=task)
    else:
        task_id = request.form['delete']
        with session as session:
            query = select(Tasks).filter(Tasks.id == task_id)
            task = session.execute(query).scalars().unique().one()
            session.delete(task)
            session.commit()
            tasks = get_tasks(session=session)
        return render_template("tasks.html", tasks=tasks)



@app.route("/delete", methods=['POST', 'GET'])
def delete():
    session = DBSession()
    task_id = request.form['delete']
    with session as session:
        query = select(Tasks).filter(Tasks.id == task_id)
        task = session.execute(query).scalars().unique().one()
        session.delete(task)
        session.commit()
        tasks = get_tasks(session=session)
    return render_template("tasks_counter.html", counter="25:00", tasks=tasks, task=task)

# @app.route("/update", methods=['POST', 'GET'])
# def update():
#     session = DBSession()


@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)



if __name__ == '__main__':
    app.run(debug=True)
