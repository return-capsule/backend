from mongoengine import *


class ImageModel(Document):
    meta = {
        'collection': 'image'
    }

    file_name = StringField(
        required=True
    )

    saved_date = DateTimeField(
        required=True
    )
