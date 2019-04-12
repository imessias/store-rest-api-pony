from flask_restful import Resource, reqparse
from flask_injector import inject
from flask_jwt import jwt_required


class UserRegister(Resource):
    DECORATORS = []
    ENDPOINT = "/register"

    @inject
    def __init__(self, user_reg_service: UserRegisterService):
        self.user_reg_service = user_reg_service

        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            "username",
            type=str,
            required=True,
            help="The field \"username\" cannot be empty!"
        )
        self.parser.add_argument(
            "password",
            type=str,
            required=True,
            help="The field \"password\" cannot be empty!"
        )

    def post(self):
        data = self.parser.parse_args()
        return self.user_reg_service.registUser(**data)


class UserLogout(Resource):
    DECORATORS = [jwt_required()]
    ENDPOINT = "/logout"

    @inject
    def __init__(self, user_logout_service: UserLogoutService):
        self.user_logout_service = user_logout_service

    def post(self):
        return self.user_logout_service.userLogout()


class User(Resource):
    DECORATORS = []
    ENDPOINT = "/user/<int:user_id>"

    @inject
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get(self, user_id: int):
        return self.user_service.getUser(user_id)

    def delete(self, user_id: int):
        return self.user_service.deleteUser(user_id)