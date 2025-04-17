from rest_framework import serializers

class ReportInputSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=['count', 'amount'])
    mode = serializers.ChoiceField(choices=['daily', 'weekly', 'monthly'])
    merchantId = serializers.CharField(required=False)