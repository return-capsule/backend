from flask import Blueprint, request, abort, Response
from flask_cors import cross_origin
from flask_restful import Api
from flask_jwt_extended import create_access_token, create_refresh_token

from app.views import BaseResource, check_json
from app.models.user import UserModel

api = Api(Blueprint(__name__, __name__))
api.prefix = "/api"


@api.resource("/login")
class UserLogin(BaseResource):

    def post(self):
        print(request.json['email'], request.json['password'])
        user = UserModel.objects(email=request.json['email'], password=request.json['password'])
        return ({
                    "access_token": str(create_access_token(request.json['email'])),
                    "refresh_token": str(create_refresh_token(request.json['email']))
                }, 200) if user else abort(401)


@api.resource("/account")
class UserSignUp(BaseResource):

    def post(self):
        payload = request.json
        data = {
            "email": payload["email"],
            "password": payload["password"],
            "name": payload["name"]
        }
        user = UserModel.objects(email=request.json['email']).first()

        if user:
            abort(409)

        UserModel(**data).save()
        return "", 201


@api.blueprint.after_request  # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response
