from rest_framework.response import Response
from rest_framework import viewsets, permissions
from django.db.models import F

from meeting_request.models import Meeting_Cater_Type, Meeting_Necessary_Equipment, Meeting_Request
from .serializers import Meeting_Cater_TypeSerializer, Meeting_Necessary_EquipmentSerializer, Meeting_RequestSerializer



class Meeting_Cater_TypeViewSet(viewsets.ModelViewSet):
    queryset = Meeting_Cater_Type.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Meeting_Cater_TypeSerializer


class Meeting_Necessary_EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Meeting_Necessary_Equipment.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Meeting_Necessary_EquipmentSerializer


class Meeting_RequestViewSet(viewsets.ModelViewSet):
    queryset = Meeting_Request.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Meeting_RequestSerializer
