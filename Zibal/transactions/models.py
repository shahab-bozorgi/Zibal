from mongoengine import Document, fields

class Transaction(Document):
    merchantId = fields.ObjectIdField(required=True)
    amount = fields.IntField(required=True)
    createdAt = fields.DateTimeField(required=True)

    meta = {
        'collection': 'transaction',
        'indexes': [
            'merchantId',
            'createdAt',
        ]
    }

class TransactionSummary(Document):
    merchantId = fields.ObjectIdField(required=True)
    mode = fields.StringField(choices=["daily", "weekly", "monthly"], required=True)
    type = fields.StringField(choices=["count", "amount"], required=True)
    data = fields.ListField(
        fields.DictField(),
        required=True
    )

    meta = {
        'collection': 'transaction_summary'
    }
