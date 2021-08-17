from src.models import db, Todo
from flask import jsonify, abort, make_response

def get_all_todos():
    todos = Todo.query.all()
    res = {}
    for todo in todos:
        res[todo.id] = {
            'title': todo.title,
            'complete': todo.complete,
        }
    return make_response(res, 200)

def get_todo_by_id(id):
    todo = Todo.query.filter_by(id=id).first()
    if not todo:
        abort(404)
    return jsonify({
        'title': todo.title,
        'complete': todo.complete,
    })

def create_a_todo(args):
    todo = Todo(title=args['title'], complete=False)
    save_database(todo)
    return make_response({
        'id': todo.id,
        'message': 'Add new todo successfully'
    }, 201)

def change_status(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.complete = not todo.complete
    save_database(todo)

    return make_response({
        'message': "Update successfully",
        'id': id
    }, 200)

def delete_todo(id):
    todo = Todo.query.filter_by(id=id).first()

    db.session.delete(todo)
    db.session.commit()

    return jsonify({
        'message': "Delete successfully",
        'id': id
    })

def save_database(todo):
    db.session.add(todo)
    db.session.commit()
