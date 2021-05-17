from rest_framework.response import Response
from rest_framework import viewsets, permissions
from django.db.models import F

from .models import Meeting_Room, Meeting_Request, Meeting_Cater_Type, Meeting_Equipment
from .serializers import Meeting_RoomSerializer, Meeting_RequestSerializer, \
    Meeting_Cater_TypeSerializer, Meeting_EquipmentSerializer



class Meeting_RoomViewSet(viewsets.ModelViewSet):
    queryset = Meeting_Room.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Meeting_RoomSerializer
    
    
class Meeting_Cater_TypeViewSet(viewsets.ModelViewSet):
    queryset = Meeting_Cater_Type.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Meeting_Cater_TypeSerializer


class Meeting_EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Meeting_Equipment.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Meeting_EquipmentSerializer


class Meeting_RequestViewSet(viewsets.ModelViewSet):
    queryset = Meeting_Request.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Meeting_RequestSerializer
