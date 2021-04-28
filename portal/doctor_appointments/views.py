from rest_framework import mixins, viewsets, status, generics, permissions, renderers
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.db.models import Q

from django.contrib.auth.models import User
from doctor_appointments.models import Doctors, DocPatients, DocPatientsFiles, DocSchedulesWeekDays, DocSchedulesDays, DocAppointmentTimes, DocAppointments
from .serializers import DoctorsSerializer, DocPatientsSerializer, DocPatientsFilesSerializer, \
    DocSchedulesWeekDaysSerializer, DocSchedulesDaysSerializer, DocAppointmentTimesSerializer, DocAppointmentsSerializer



class DoctorsViewSet(viewsets.ModelViewSet):
    queryset = Doctors.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = DoctorsSerializer


class DocPatientsViewSet(viewsets.ModelViewSet):
    queryset = DocPatients.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = DocPatientsSerializer


class PatientsFileUploadViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = DocPatientsFiles.objects.all()
    permission_classes = [
    permissions.IsAuthenticated]

    parser_classes = (MultiPartParser, FormParser)
    def get(self, request, *args, **kwargs):
        queryset = DocPatientsFiles.objects.all()
        serializer = DocPatientsFilesSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        PatientsFiles_serializer = DocPatientsFilesSerializer(data=request.data)
        if PatientsFiles_serializer.is_valid():
            PatientsFiles_serializer.save()
            return Response(PatientsFiles_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(PatientsFiles_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    serializer_class = DocPatientsFilesSerializer    


class DocPatientsFilesViewSet(viewsets.ModelViewSet):
    queryset = DocPatientsFiles.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = DocPatientsFilesSerializer


class DocSchedulesWeekDaysViewSet(viewsets.ModelViewSet):
    queryset = DocSchedulesWeekDays.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = DocSchedulesWeekDaysSerializer


class DocSchedulesDaysViewSet(viewsets.ModelViewSet):
    queryset = DocSchedulesDays.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = DocSchedulesDaysSerializer


class DocAppointmentTimesViewSet(viewsets.ModelViewSet):
    queryset = DocAppointmentTimes.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = DocAppointmentTimesSerializer        


class FilteredAppointmentTimesViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DocAppointmentTimesSerializer     
       
    def get_queryset(self):
        userID = self.kwargs['id']

        if(userID == 1):
            return DocAppointmentTimes.objects.all()
        else:
            user = User.objects.get(pk=userID)
            usergrouppermissions = []
            usergroups = []
            for group in user.groups.all():
                if(group not in usergroups):
                        usergroups.append(group.id)
                for permission in group.permissions.all():
                    if(permission not in usergrouppermissions):
                        usergrouppermissions.append(permission.id)
            
            for permission in user.user_permissions.all():
                if(permission not in usergrouppermissions):
                    usergrouppermissions.append(permission.id)

            if(89 in usergrouppermissions or 93 in usergrouppermissions):   #Can add doc schedules days & Can add doc schedules week days
                return DocAppointmentTimes.objects.all()
            else:
                c1 = Q(schedulesDay__schedulesWeekDay__doctor__employee__user=userID) 
                return DocAppointmentTimes.objects.filter(c1)


class DocAppointmentsViewSet(viewsets.ModelViewSet):
    queryset = DocAppointments.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = DocAppointmentsSerializer        


