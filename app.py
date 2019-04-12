from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_injector import FlaskInjector, singleton
from code.api import API_HANDLERS
from code.model.entities import Database
from code.service import SERVICES
#from .security import Security
import os


app = Flask(__name__)
CORS(app)
api = Api(app=app)

for handler in API_HANDLERS:
    handler.decorators = handler.DECORATORS
    api.add_resource(handler, handler.ENDPOINT)

def configure(binder):
    PROVIDER = "sqlite"
    FILE_NAME = os.path.join("..", "..", "data", "database.sqlite")
    create_db = True

    args = {
        "provider": PROVIDER,
        "filename": FILE_NAME,
        "create_db": create_db
    }

    db = Database(**args)
    db.model.generate_mapping(create_tables=True)
    binder.bind(Database, to=db, scope=singleton)

    for service in SERVICES:
        binder.bind(service, scope=singleton)

    #binder.bind(Security, scope=singleton)


injector = FlaskInjector(app=app, modules=[configure])
#security: Security = injector.injector.get(Security)

app.secret_key = "pocosi12!"
app.config["JWT_AUTH_URL_RULE"] = "/login"
#jwt = JWT(app, security.authenticate, security.identity)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)