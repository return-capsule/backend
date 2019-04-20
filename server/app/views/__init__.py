import boto3, botocore

from functools import wraps

from flask import current_app, abort, request
from flask_restful import Resource

from app.config import Config


def upload_file_to_s3(file, bucket_name, acl="public-read", access_key_id=Config.S3_KEY,
                      secret_access_key=Config.S3_SECRET):
    # s3.upload_fileobj(file, bucket_name, file.filename,
    #                   ExtraArgs={
    #                       "ACL": acl,
    #                       "ContentType": file.content_type
    #                   })
    # return f"{current_app.config['S3_URL']}/{file.filename}"

    s3 = boto3.client(
        's3',
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key
    )

    try:

        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e

    return f"{current_app.config['S3_URL']}/{file.filename}"


def check_json(keys):
    def decorator(original_func):

        @wraps(original_func)
        def wrapper(*args, **kwargs):
            if not request.is_json:
                abort(406)
            for k, t in keys.items():
                if k not in request.json or type(request.json[k]) is not t:
                    print(k)
                    abort(400)
            return original_func(*args, **kwargs)

        return wrapper

    return decorator


class BaseResource(Resource):

    @classmethod
    def unicode_safe_json_dumps(cls):
        pass


class Router:

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        from app.views import auth, capsule
        app.register_blueprint(auth.api.blueprint)
        app.register_blueprint(capsule.api.blueprint)
