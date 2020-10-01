import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=float, required=True, help="This field cannot be left blank!")

    @jwt_required()
    def get(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}

        return {'message': 'Item not found'}

    def post(self, name):
        pass

    def delete(self, name):
        pass

    def put(self, name):
        pass


class ItemList(Resource):
    pass
