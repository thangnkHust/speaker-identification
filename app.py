# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Todo(db.Model):
#     id = db.Column('id', db.Integer, primary_key=True)
#     title = db.Column('title', db.String(100))
#     complete = db.Column('complete', db.Boolean)

#     def __init__(self, title, complete):
#         self.title = title
#         self.complete = complete

# @app.route("/todo")
# def index():
#     todo_list = Todo.query.all()
#     return todo_list

# @app.route('/test')
# def about():
#     return render_template('index.html', title='Todo List', name='Nguyen Khac Thang')
from my_app import app
# from my_app.todo.models import Todo
# from my_app import db

if __name__ == "__main__":
    # db.create_all()
    # new_todo = Todo(title="todo 1", complete=False)

    # db.session.add(new_todo)
    # db.session.commit()

    app.run(host="0.0.0.0")
