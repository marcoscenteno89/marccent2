from portfolio.models import Contact
from rest_framework import viewsets, permissions
from .serializers import portfolioSerializer

class portfolioViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = portfolioSerializer