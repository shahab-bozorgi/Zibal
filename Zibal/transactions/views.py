from bson import ObjectId
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TransactionSummary
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




class FastTransactionReportView(APIView):
    serializer_class = ReportInputSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        # تبدیل merchantId به ObjectId در صورتی که رشته باشد
        try:
            merchant_id = ObjectId(data['merchantId'])
        except Exception as e:
            raise NotFound(detail="Merchant ID is invalid or not found")

        # جستجو در پایگاه داده برای داده‌های خلاصه
        summary = TransactionSummary.objects(
            merchantId=merchant_id,
            mode=data['mode'],
            type=data['type']
        ).first()

        # اگر داده‌ای یافت نشد، یک پیغام مناسب به کاربر نمایش داده می‌شود
        if summary:
            return Response(summary.data)
        else:
            return Response([], status=404)
