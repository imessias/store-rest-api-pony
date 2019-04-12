from pony.orm import *
from pony.orm import Database as PonyDatabase
from decimal import Decimal


class Database:
    def __init__(self, **db_params):
        self.model = PonyDatabase(**db_params)

        class User(self.model.Entity):
            id = PrimaryKey(int, auto=True)
            username = Required(str, unique=True)
            password = Required(str)

        class Store(self.model.Entity):
            id = PrimaryKey(int, auto=True)
            name = Required(str, 80)
            items = Set("Item")

        class Item(self.model.Entity):
            id = PrimaryKey(int, auto=True)
            name = Required(str, 80)
            price = Required(Decimal, precision=2)
            store = Required("Store")
