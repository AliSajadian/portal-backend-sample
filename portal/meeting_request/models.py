from django.db import models
from baseInfo.models import Department, Employee
from datetime import datetime


class Meeting_Room_Type(models.Model):
    name = models.CharField(max_length=50)
    objects = models.Manager()

    class Meta:
        db_table = 'tbl_meeting_room_type'

class Meeting_Equipment(models.Model):
    name = models.CharField(max_length=100)
    fixed = models.BooleanField(default=False)
    objects = models.Manager()  

    class Meta:
        db_table = "tbl_meeting_equipment"  

class Meeting_Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    room_type = models.ForeignKey(Meeting_Room_Type, 
        related_name='room_type', on_delete=models.CASCADE, null=True)
    equipments = models.ManyToManyField(Meeting_Equipment, 
        related_name='equipments', through='Meeting_Room_Equipment')
    objects = models.Manager()

    class Meta:
        db_table = 'tbl_meeting_room'
        
class Meeting_Room_Equipment(models.Model):
    room = models.ForeignKey(Meeting_Room, 
        related_name="room", on_delete=models.CASCADE, null=True)
    equipment = models.ForeignKey(Meeting_Equipment, 
        related_name="equipment", on_delete=models.CASCADE, null=True)
    qty = models.PositiveSmallIntegerField(null=True)
    description = models.CharField(max_length=500, null=True)
    objects = models.Manager()  

    class Meta:
        unique_together = [['room', 'equipment']]
        db_table = "tbl_meeting_room_equipment"

class Meeting_Cater_Type(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()  

    class Meta:
        db_table = "tbl_meeting_cater_type"

class Meeting_Request(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now, blank=True)
    start_hour= models.TimeField(auto_now=False, auto_now_add=False)
    end_hour = models.TimeField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=500)
    requester = models.ForeignKey(Employee, 
        related_name="employee", on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department,
        related_name="department", on_delete=models.CASCADE, null=True)
    confirm = models.BooleanField(default=False)
    meeting_room = models.ForeignKey(Meeting_Room, 
        related_name="romm", on_delete=models.CASCADE, null=True)
    cater_types = models.ManyToManyField(Meeting_Cater_Type, 
    related_name='cater_types', through='Meeting_Request_Cater_Type')

    objects = models.Manager()  

    class Meta:
        db_table = "tbl_meeting_request"

class Meeting_Request_Cater_Type(models.Model):
    request = models.ForeignKey(Meeting_Request, 
        related_name='request', on_delete=models.CASCADE, null=True)        
    cater_type = models.ForeignKey(Meeting_Cater_Type, 
        related_name='cater_type', on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=500, null=True)
    objects = models.Manager()  

    class Meta:
        unique_together = [['request', 'cater_type']]
        db_table = "tbl_meeting_request_cater_type"
