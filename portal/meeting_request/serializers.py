from rest_framework import serializers

from .models import Meeting_Room, Meeting_Request, Meeting_Cater_Type, Meeting_Equipment


class Meeting_RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting_Room
        fields = '__all__'

class Meeting_Cater_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting_Cater_Type
        fields = '__all__'

class Meeting_EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting_Equipment
        fields = '__all__'

class Meeting_RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting_Request
        fields = '__all__'

