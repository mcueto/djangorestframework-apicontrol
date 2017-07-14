"""API Control views."""
from rest_framework import viewsets
from .models import (
    App,
    OrganizationalUnitType,
    OrganizationalUnit
)
from .serializers import (
    AppSerializer,
    OrganizationalUnitTypeSerializer,
    OrganizationalUnitSerializer
)


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer


class OrganizationalUnitTypeViewSet(viewsets.ModelViewSet):
    queryset = OrganizationalUnitType.objects.all()
    serializer_class = OrganizationalUnitTypeSerializer


class OrganizationalUnitViewSet(viewsets.ModelViewSet):
    queryset = OrganizationalUnit.objects.all()
    serializer_class = OrganizationalUnitSerializer
