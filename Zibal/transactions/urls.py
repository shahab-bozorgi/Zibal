from django.urls import path
from .views import FastTransactionReportView

urlpatterns = [
    path('api/transaction-report/', FastTransactionReportView.as_view())
]
