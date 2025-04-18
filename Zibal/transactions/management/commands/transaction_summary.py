from django.core.management.base import BaseCommand
from mongoengine import connect, disconnect
from transactions.models import Transaction, TransactionSummary
from datetime import datetime

class Command(BaseCommand):
    help = "Generates summarized transaction data and stores in `transaction_summary` collection"

    def handle(self, *args, **options):
        disconnect()
        connect(
            alias='default',
            db='zibal_db',
            host='mongodb://shahab:123@localhost:27017/zibal_db?authSource=admin'
        )

        TransactionSummary.objects.delete()
        print("Deleted old summaries.")

        modes = ['daily', 'weekly', 'monthly']
        types = ['amount', 'count']

        for mode in modes:
            for summary_type in types:
                pipeline = self.get_pipeline(mode, summary_type)
                results = list(Transaction.objects.aggregate(pipeline))

                print(f"{mode.upper()} | {summary_type.upper()} - {len(results)} entries")

                for item in results:
                    TransactionSummary(
                        merchantId=item['merchantId'],
                        mode=mode,
                        type=summary_type,
                        data=item['data']
                    ).save()

        print("✅ All summaries generated successfully.")

    def get_pipeline(self, mode, summary_type):
        group_by = {}
        if mode == 'daily':
            group_by = {
                "merchantId": "$merchantId",
                "year": {"$year": "$createdAt"},
                "month": {"$month": "$createdAt"},
                "day": {"$dayOfMonth": "$createdAt"},
            }
        elif mode == 'weekly':
            group_by = {
                "merchantId": "$merchantId",
                "year": {"$year": "$createdAt"},
                "week": {"$isoWeek": "$createdAt"},
            }
        elif mode == 'monthly':
            group_by = {
                "merchantId": "$merchantId",
                "year": {"$year": "$createdAt"},
                "month": {"$month": "$createdAt"},
            }

        value_field = "$amount" if summary_type == 'amount' else 1

        return [
            {
                "$group": {
                    "_id": group_by,
                    "value": {"$sum": value_field}
                }
            },
            {
                "$group": {
                    "_id": "$_id.merchantId",
                    "data": {
                        "$push": {
                            "key": {
                                "$concat": [
                                    {"$toString": "$_id.year"},
                                    "-",
                                    {"$toString": "$_id.month" if mode != 'weekly' else "$_id.week"},
                                    *(["-", {"$toString": "$_id.day"}] if mode == 'daily' else [])
                                ]
                            },
                            "value": "$value"
                        }
                    }
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "merchantId": "$_id",
                    "data": 1
                }
            }
        ]