from django.apps import AppConfig
from mongoengine import connect

from Zibal import settings


class TransactionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transactions'
    def ready(self):
        mongodb_settings = settings.MONGODB
        connect(
            db=mongodb_settings['db'],
            host=mongodb_settings['host'],
            port=mongodb_settings['port'],
            username=mongodb_settings['username'],
            password=mongodb_settings['password'],
            authentication_source=mongodb_settings['authentication_source']
        )