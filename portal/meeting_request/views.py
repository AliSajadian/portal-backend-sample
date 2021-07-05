from rest_framework import response
from rest_framework.response import Response
from rest_framework import generics, viewsets, permissions, status
from django.db.models import F

from .models import Meeting_Room, Meeting_Room_Type, Meeting_Request, Meeting_Cater_Type, Meeting_Equipment, \
    Meeting_Room_Equipment, Meeting_Request_Cater_Type, Meeting_Request_Equipment
from .serializers import Meeting_RoomSerializer, Meeting_Room_TypeSerializer, Meeting_RequestSerializer, \
    Meeting_Cater_TypeSerializer, Meeting_EquipmentSerializer, Meeting_Request_Cater_TypeSerializer
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

class Meeting_Request_Cater_TypeViewSet(viewsets.ModelViewSet):
    queryset = Meeting_Request.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = Meeting_Request_Cater_TypeSerializer

class Meeting_DateRequestsAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            requester = data["requester"]
            selectedDate = data['date']
            date = datetime.strptime(selectedDate, '%Y-%m-%d').date()

            result1 = Meeting_Request.objects.filter(date__exact=date, confirm__exact=True).values('id', 'title', 'date', 
                        'description', 'confirm', 'department_id', 'meeting_room_id', 'requester_id',  'meeting_member_no', 'start_hour', 'end_hour', 
                        'meeting_room__room_type_id', 'department__company__id', 'department__company__name', 'department__name', 'meeting_room__name')
            result2 = Meeting_Request.objects.filter(requester_id__exact=requester, date__exact=date, confirm__exact=False).values('id', 'title', 'date', 
                        'description', 'confirm', 'department_id', 'meeting_room_id', 'requester_id', 'meeting_member_no', 'start_hour', 'end_hour', 
                        'meeting_room__room_type_id', 'department__company__id', 'department__company__name', 'department__name', 'meeting_room__name')
            result = result1.union(result2)

            return Response(result)
        except Exception as e:
            return Response(e)

class GetRequest_Cater_TypesAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        try:
            request_id = self.kwargs['id']
            result = Meeting_Request_Cater_Type.objects.filter(request_id__exact=request_id).values('id', 'request_id', 'cater_type_id', 'description')
            return Response(result)
        except Exception as e:
            return Response(
                {
                    "Failure": str(e) 
                },
                status=status.HTTP_400_BAD_REQUEST
            ) 

class GetRequest_EquipmentsAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        try:
            request_id = self.kwargs['id']
            result = Meeting_Request_Equipment.objects.filter(request_id__exact=request_id).values('id', 'request_id', 'equipment_id', 'qty', 'description')
            return Response(result)
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

class Meeting_Room_EquipmentAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request, *args, **kwargs):
        try:
            id = self.kwargs["id"]
            results = Meeting_Room_Equipment.objects.filter(
                room_id__exact=id).select_related('equipment').filter(
                    equipment__fixed__exact=True).values('room_id', 'equipment__name', 'qty', 'description')
            return Response(results)
        except Exception as e:
            return Response(
                {
                    "Failure" : str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class SaveMeeting_RequestAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            id = data["request_id"]
            title = data["title"]
            date = data["date"]
            start_hour = data["start_hour"]
            end_hour = data["end_hour"]
            description = data["description"]
            confirm = data["confirm"]
            department = data["department"]
            meeting_room = data["meeting_room"]
            requester = data["requester"]
            meeting_member_no = data["meeting_member_no"]
            requestCaterTypes = data["requestCaterTypes"]
            requestEquipments = data["requestEquipments"]
            editMood = data["editMood"]

            if(editMood == 1):
                meeting_request = Meeting_Request(title=title, date=date, start_hour=start_hour, end_hour=end_hour, description=description, 
                                    confirm=confirm, department_id=department, meeting_room_id=meeting_room, requester_id=requester, 
                                    meeting_member_no=meeting_member_no)
                meeting_request.save()
                request_id = meeting_request.id

                Meeting_Request_Cater_Type.objects.filter(request=request_id).delete()
                for requestCaterType in requestCaterTypes:
                    meeting_request_cater_type = Meeting_Request_Cater_Type(
                                                        request_id=request_id, 
                                                        cater_type_id=requestCaterType["cater_type_id"],
                                                        description=requestCaterType["description"])
                    meeting_request_cater_type.save()

                Meeting_Request_Equipment.objects.filter(request=request_id).delete()
                for requestEquipment in requestEquipments:
                    meeting_request_equipment = Meeting_Request_Equipment(
                                                        request_id=request_id, 
                                                        equipment_id=requestEquipment["equipment_id"],
                                                        description=requestEquipment["description"],
                                                        qty=requestEquipment["qty"])                                          
                    meeting_request_equipment.save()

                results = Meeting_Request.objects.filter(pk=request_id).values('id', 'title', 'date', 
                        'description', 'confirm', 'department_id', 'meeting_room_id', 'requester_id', 'meeting_member_no', 'start_hour', 'end_hour', 
                        'meeting_room__room_type_id', 'department__company__id', 'department__company__name', 'department__name', 'meeting_room__name')
                return Response(results[0])

            elif(editMood == 2):
                meeting_request = Meeting_Request.objects.get(pk=id)
                meeting_request.title = title
                meeting_request.date = date
                meeting_request.start_hour = start_hour
                meeting_request.end_hour = end_hour
                meeting_request.description = description
                meeting_request.confirm = confirm
                meeting_request.department_id = department
                meeting_request.meeting_room_id = meeting_room
                meeting_request.requester_id = requester
                meeting_request.meeting_member_no = meeting_member_no
                meeting_request.save()
                
                Meeting_Request_Cater_Type.objects.filter(request=id).delete()
                for requestCaterType in requestCaterTypes:
                    meeting_request_cater_type = Meeting_Request_Cater_Type(
                                                        request_id=id, 
                                                        cater_type_id=requestCaterType["cater_type_id"],
                                                        description=requestCaterType["description"])
                    meeting_request_cater_type.save()

                Meeting_Request_Equipment.objects.filter(request=id).delete()
                for requestEquipment in requestEquipments:
                    meeting_request_equipment = Meeting_Request_Equipment(
                                                        request_id=id, 
                                                        equipment_id=requestEquipment["equipment_id"],
                                                        description=requestEquipment["description"],
                                                        qty=requestEquipment["qty"])                                                  
                    meeting_request_equipment.save()

                results = Meeting_Request.objects.filter(pk=id).values('id', 'title', 'date', 
                        'description', 'confirm', 'department_id', 'meeting_room_id', 'requester_id', 'meeting_member_no', 'start_hour', 'end_hour', 
                        'meeting_room__room_type_id', 'department__company__id', 'department__company__name', 'department__name', 'meeting_room__name')
                return Response(results[0])
            return Response({'error'})
        except Exception as e:
            return Response(e)
          

