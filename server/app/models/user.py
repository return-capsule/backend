from mongoengine import *


class UserModel(Document):
    meta = {
        'collection': 'user'
    }

    email = StringField(
        primary_key=True
    )

    password = StringField(
        required=True
    )

    name = StringField(
        required=True
    )
