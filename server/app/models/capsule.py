from mongoengine import *

from app.models.image import ImageModel


class CapsuleModel(Document):
    meta = {
        'collection': 'capsule'
    }

    user_email = StringField(
        required=True
    )

    changeable = StringField(
        required=True
    )

    images = ListField(
        required=True
    )

    text = StringField(
        required=False
    )

    posted_date = DateTimeField(
        required=True
    )

    open_date = DateTimeField(
        required=True
    )
