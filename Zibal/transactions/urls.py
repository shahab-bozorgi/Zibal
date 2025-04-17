from django.urls import path
from .views import TransactionReportView

urlpatterns = [
    path('api/transaction-report/', TransactionReportView.as_view())
]
