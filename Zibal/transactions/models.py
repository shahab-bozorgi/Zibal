from mongoengine import Document, fields

class Transaction(Document):
    merchantId = fields.StringField(required=True)
    amount = fields.IntField(required=True)
    createdAt = fields.DateTimeField(required=True)

    meta = {
        'indexes': [
            'merchantId',
            'createdAt',
        ]
    }
