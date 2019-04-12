from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flask_injector import inject

class Item(Resource):
    DECORATORS = [jwt_required()]
    ENDPOINT = "/item/<string:name>"

    @inject
    def __init__(self, item_service: ItemService):
        self.item_service = item_service

        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            "price",
            type=float,
            required=True,
            help="The \"price\" field cannot be left blank!"
        )
        self.parser.add_argument(
            "store_id",
            type=str,
            required=True,
            help="Cannot insert item without a store ID!"
        )

    def get(self, name):
        return self.item_service.getItem(name)

    def post(self, name):
        args = self.parser.parse_args()
        return self.item_service.postItem(name, **args)

    def delete(self, name):
        return self.item_service.deleteItem(name)

    def put(self, name):
        args = self.parser.parse_args()
        return self.item_service.updateItem(name, **args)


class ItemList(Resource):
    DECORATORS = [jwt_required()]
    ENDPOINT = "/items"

    @inject
    def __init__(self, item_list_service: ItemListService):
        self.item_list_service = item_list_service

    def get(self):
        return self.item_list_service.getItems()
