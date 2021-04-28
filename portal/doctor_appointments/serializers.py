from rest_framework import serializers

from doctor_appointments.models import Doctors, DocPatients, DocPatientsFiles, DocSchedulesWeekDays, DocSchedulesDays, DocAppointmentTimes, DocAppointments



class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'

class DocPatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocPatients
        fields = '__all__'        

class DocPatientsFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocPatientsFiles
        fields = '__all__' 

class DocSchedulesWeekDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocSchedulesWeekDays
        fields = '__all__'


class DocSchedulesDaysSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = DocSchedulesDays
        fields = '__all__'


class DocAppointmentTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocAppointmentTimes
        fields = '__all__'


class DocAppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocAppointments
        fields = '__all__'        