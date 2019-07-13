from portfolio.models import portfolio
from rest_framework import viewsets, permissions
from .serializers import portfolioSerializer

class portfolioViewSet(viewsets.ModelViewSet):
    queryset = portfolio.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = portfolioSerializer