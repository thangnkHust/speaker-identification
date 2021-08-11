import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.todo.models import Todo

todo = Blueprint('todo', __name__)

@todo.route('/')
@todo.route('/home')
def home():
    return "Welcome to my test app"

class TodoView(MethodView):

    def get(self, id=None, page=1):
        if not id:
            todos = Todo.query.paginate(page, 10).items
            res = {}
            for todo in todos:
                res[todo.id] = {
                    'title': todo.title,
                    'complete': todo.complete,
                }
        else:
            todo = Todo.query.filter_by(id=id).first()
            if not todo:
                abort(404)
            res = {
                'title': todo.title,
                'complete': todo.complete,
            }
        return jsonify(res)

    def post(self):
        title = request.form.get('title')

        todo = Todo(title=title, complete=False)

        db.session.add(todo)
        db.session.commit()

        return jsonify({todo.id: {
            'title': todo.title,
            'complete': todo.complete,
        }})

    def put(self, id):
        todo = Todo.query.filter_by(id=id).first()
        todo.complete = not todo.complete

        db.session.commit()

        return jsonify(
            {
                'message': "Update successfuly",
                'id': id
            }
        )

    def delete(self, id):
        todo = Todo.query.filter_by(id=id).first()

        db.session.delete(todo)
        db.session.commit()

        return jsonify(
            {
                'message': "Delete successfuly",
                'id': id
            }
        )

todo_view =  TodoView.as_view('todo_view')
app.add_url_rule(
    '/todo', view_func=todo_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/todo/<int:id>', view_func=todo_view, methods=['GET', 'PUT', 'DELETE']
)