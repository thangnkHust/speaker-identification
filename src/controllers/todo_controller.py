from flask_restful import Resource, reqparse
from flask import request
from src.services.todo_service import get_all_todos, get_todo_by_id, create_a_todo, change_status, delete_todo

parser = reqparse.RequestParser()

class Hello(Resource):
    def get(self):
        return 'hello'

class TodoList(Resource):
    def get(self):
        return get_all_todos()
    
    def post(self):
        parser.add_argument('title')
        args = parser.parse_args()

        return create_a_todo(args)

class Todo(Resource):
    def get(self, id):
        return get_todo_by_id(id=id)

    def put(self, id):
        return change_status(id=id)
    
    def delete(self, id):
        return delete_todo(id)
