from rest_framework import serializers
from portfolio.models import Contact

class portfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'