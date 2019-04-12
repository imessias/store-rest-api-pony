from flask_injector import inject
from pony.orm import db_session
from code.model.entities import Database


class StoreService:
    @inject
    def __init__(self, db: Database):
        self.db = db

    @db_session
    def get_store(self, name):
        store = self.db.model.Store.get(lambda s: s.name == name)
        if store:
            return store.to_dict()
        return {"message": "Store not found."}, 404

    @db_session
    def create_store(self, name):
        if not self.db.model.Store.exists(lambda s: s.name == name):
            return self.db.model.Store(
                name=name
            )
        return {"message": "An error occurred creating the store."}, 500

    @db_session
    def delete_stores(self, name):
        store = self.db.model.Store.get(lambda s: s.name == name)
        if store:
            store.delete()
        return {"message": "Store deleted."}


class StoreListService:
    @inject
    def __init__(self, db: Database):
        self.db = db

    @db_session
    def get_stores(self):
        stores = self.db.model.Store.select()
        store_list = [store.to_dict() for store in stores]
        return store_list