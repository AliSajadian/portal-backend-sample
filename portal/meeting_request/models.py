from django.db import models
from baseInfo.models import Employee
from datetime import datetime


class Meeting_Room(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()

    class Meta:
        db_table = 'tbl_meeting_room'

class Meeting_Cater_Type(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()  

    class Meta:
        db_table = "tbl_meeting_cater_type"

class Meeting_Necessary_Equipment(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()  

    class Meta:
        db_table = "tbl_meeting_necessary_equipment"     

class Meeting_Request(models.Model):
    date = models.DateField(default=datetime.now, blank=True)
    start_hour= models.TimeField(auto_now=False, auto_now_add=False)
    end_hour = models.TimeField(auto_now=False, auto_now_add=False)
    requester = models.ForeignKey(Employee, 
        related_name="employee_meeting_request", on_delete=models.CASCADE)
    meeting_room = models.ForeignKey(Meeting_Room, 
        related_name="meeting_room_meeting_request", on_delete=models.CASCADE)
    cater_types = models.ManyToManyField(Meeting_Cater_Type, related_name='cater_types')
    necessary_equipments = models.ManyToManyField(Meeting_Necessary_Equipment, related_name='necessary_equipments')

    objects = models.Manager()  

    class Meta:
        db_table = "tbl_meeting_request"