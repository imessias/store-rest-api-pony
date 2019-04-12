from flask_restful import Resource
from flask_injector import inject
from flask_jwt import jwt_required
from code.service.StoreService import StoreService, StoreListService


class Store(Resource):
    DECORATORS = [jwt_required()]
    ENDPOINT = "/store/<string:name>"

    @inject
    def __init__(self, store_service: StoreService):
        self. store_service = store_service

    def get(self, name):
        return self.store_service.get_store(name)

    def post(self, name):
        return self.store_service.create_store(name)

    def delete(self, name):
        return self.store_service.delete_store(name)


class StoreList(Resource):
    DECORATORS = []
    ENDPOINT = "/stores"

    @inject
    def __init__(self, store_list_service: StoreListService):
        self.store_list_service = store_list_service

    def get(self):
        return self.store_list_service.get_stores()
