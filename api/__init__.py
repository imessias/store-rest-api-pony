from .ItemAPI import Item, ItemList
from .StoreAPI import Store, StoreList
from .UserAPI import UserRegister, UserLogout, User

API_HANDLERS = [
    Item,
    ItemList,
    Store,
    StoreList,
    UserRegister,
    UserLogout,
    User
]