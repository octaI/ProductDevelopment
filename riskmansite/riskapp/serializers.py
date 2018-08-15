from .models import RiskEntries, RiskTypes
from rest_framework import serializers


class RiskEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskEntries
        fields = ('id', 'insurer_id', 'code', 'date', 'risk_data')


class RiskTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskTypes
        fields = '__all__'
