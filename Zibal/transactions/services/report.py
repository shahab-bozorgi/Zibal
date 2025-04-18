import pytz
from bson import ObjectId
from mongoengine.connection import get_db

def generate_transaction_report(data):
    db = get_db()
    merchant_id = ObjectId(data['merchantId'])
    mode = data['mode']
    tz = pytz.timezone('Asia/Tehran')

    date_expr = {
        'daily': {'$dateToString': {'format': '%Y/%m/%d', 'date': '$createdAt', 'timezone': 'Asia/Tehran'}},
        'weekly': {'$dateToString': {'format': '%G-W%V', 'date': '$createdAt', 'timezone': 'Asia/Tehran'}},
        'monthly': {'$dateToString': {'format': '%Y-%m', 'date': '$createdAt', 'timezone': 'Asia/Tehran'}}
    }[mode]

    group_expr = {
        '_id': date_expr,
        'value': {'$sum': '$amount'} if data['type'] == 'amount' else {'$sum': 1}
    }

    pipeline = [
        {'$match': {'merchantId': merchant_id}},
        {'$group': group_expr},
        {'$sort': {'_id': 1}},
        {'$project': {'key': '$_id', 'value': 1, '_id': 0}},
    ]

    result = list(db.transaction.aggregate(pipeline))
    return result


