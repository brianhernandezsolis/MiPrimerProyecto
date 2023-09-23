from rest_framework import viewsets, permissions
from .serializers import PaisSerializer, DepartamentoSerializer, MunicipioSerializer
from .models import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    permission_classes = [permissions.IsAuthenticated]  
    authentication_classes = [SessionAuthentication, BasicAuthentication]

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]