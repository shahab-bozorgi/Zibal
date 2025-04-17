from bson import ObjectId
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction
import pytz

from .serializers import ReportInputSerializer
from .services.report import generate_transaction_report


class TransactionReportView(APIView):
    serializer_class = ReportInputSerializer
    def post(self, request):
        serializer = ReportInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        report = generate_transaction_report(data)
        return Response(report)

