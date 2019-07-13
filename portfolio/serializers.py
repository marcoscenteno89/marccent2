from rest_framework import serializers
from portfolio.models import portfolio

class portfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = portfolio
        fields = '__all__'