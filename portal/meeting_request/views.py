from rest_framework.response import Response
from rest_framework import generics, viewsets, permissions, status
from django.db.models import F

from .models import Meeting_Room, Meeting_Room_Type, Meeting_Request, Meeting_Cater_Type, Meeting_Equipment
from .serializers import Meeting_RoomSerializer, Meeting_Room_TypeSerializer, Meeting_RequestSerializer, \
    Meeting_Cater_TypeSerializer, Meeting_EquipmentSerializer
    # , Request_Cater_TypeSerializer
from datetime import datetime


class Meeting_Room_TypeViewSet(viewsets.ModelViewSet):
    queryset = Meeting_Room_Type.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Meeting_Room_TypeSerializer
    
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

class Meeting_DateRequestsAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        try:
            selectedDate = self.kwargs['date']
            date = datetime.strptime(selectedDate, '%Y-%m-%d').date()

            result = Meeting_Request.objects.filter(date__exact=date).values('id', 'requester',  
                        'department__company__name', 'department__name', 'meeting_room__name', 'start_hour', 'end_hour')
            return Response(result)
        except Exception as e:
            return Response(e)

class GetRequest_Cater_TypesAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        try:
            selectedDate = self.kwargs['date']
            date = datetime.strptime(selectedDate, '%Y-%m-%d').date()

            result = Meeting_Request.objects.filter(date__exact=date).values('id', 'cater_types__id', 'cater_types__name')
            return Response(result)
            
            # meeting_requests = Meeting_Request.objects.filter(date__exact=date)
            # serializer = Request_Cater_TypeSerializer(meeting_requests)
            # return Response(serializer.data)
        except Exception as e:
            return Response(
                {
                    "Failure": str(e) 
                },
                status=status.HTTP_400_BAD_REQUEST
            ) 

class PutRequest_Cater_TypesAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def put(self, request, pk, format=None):
        meeting_request = Meeting_Request.objects.get(pk=pk)
        serializer = Request_Cater_TypeSerializer(meeting_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


