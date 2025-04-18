from django.urls import path
from .views import TransactionReportView, FastTransactionReportView

urlpatterns = [
    path('api/transaction-report/', FastTransactionReportView.as_view())
]
