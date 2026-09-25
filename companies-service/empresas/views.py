from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Company
from .serializers import CompanySerializer
from .authentication import FirebaseAuthentication


class CompanyViewSet(viewsets.ModelViewSet):
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Company.objects.all()
    serializer_class = CompanySerializer