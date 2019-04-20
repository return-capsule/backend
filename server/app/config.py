import os
from datetime import timedelta


class Config:
    HOST = "0.0.0.0"
    PORT = "5001"
    DEBUG = True

    RUN_SETTING = {
        "host": HOST,
        "port": PORT,
        "debug": DEBUG
    }

    SECRET_KEY = os.getenv('SECRET_KEY')

    MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
    MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

    JWT_HEADER_TYPE = 'JWT'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=1)

    S3_BUCKET = os.environ.get("S3_BUCKET_NAME")
    S3_LOCATION = "ap-northeast-2"

    S3_KEY = os.environ.get("S3_ACCESS_KEY")
    S3_SECRET = os.environ.get("S3_SECRET_ACCESS_KEY")
    S3_URL = f"http://{S3_LOCATION}.s3.amazonaws.com/{S3_BUCKET}"

    JSON_AS_ASCII = False
