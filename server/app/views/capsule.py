import boto3

from datetime import datetime
from flask import Blueprint, request, abort, current_app
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename

from app.views import BaseResource, upload_file_to_s3
from app.models.user import UserModel
from app.models.image import ImageModel
from app.models.capsule import CapsuleModel

api = Api(Blueprint(__name__, __name__))
api.prefix = '/api'


@api.resource('/capsule')
class CapsuleController(BaseResource):

    @jwt_required
    def get(self):
        if UserModel.objects(email=get_jwt_identity()).first():
            return [{
                "capsule_id": capsule.id,
                "changeable": capsule['changeable'],
                "images": [ImageModel.objects.get(id=index) for index in capsule['images']]
            } for capsule in CapsuleModel.objects(user_email=get_jwt_identity())], 201
        else:
            return '', 401

    @jwt_required
    def post(self):
        data = request.form
        images = request.files.getlist('images')
        image_index = []

        for img in images:
            print(img)
            upload_file_to_s3(img, current_app.config['S3_BUCKET'])
            image = ImageModel(file_name=img.filename, saved_date=datetime.now())
            image.save()
            image_index.append(image.id)

        CapsuleModel(changeable=data['changeable'], user_email=get_jwt_identity(), images=image_index,
                     text=data['memory'], posted_date=datetime.now(),
                     open_date=data['open_date']).save()

        return '', 201

    def delete(self):
        pass

    def put(self):
        pass
