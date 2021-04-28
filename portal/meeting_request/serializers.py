from rest_framework import serializers

from meeting_request.models import Meeting_Cater_Type, Meeting_Necessary_Equipment, Meeting_Request



class Meeting_Cater_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting_Cater_Type
        fields = '__all__'

class Meeting_Necessary_EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting_Necessary_Equipment
        fields = '__all__'

class Meeting_RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting_Request
        fields = '__all__'

