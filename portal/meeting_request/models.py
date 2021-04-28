from django.db import models
from baseInfo.models import Employee
from datetime import datetime



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
    personel_no = models.PositiveSmallIntegerField()
    employee = models.ForeignKey(Employee, 
        related_name="employee_meeting_request", on_delete=models.CASCADE)
    cater_type = models.ForeignKey(Meeting_Cater_Type, 
        related_name="meeting_request_cater_type", on_delete=models.CASCADE)
    necessary_equipment = models.ForeignKey(Meeting_Necessary_Equipment, 
        related_name="meeting_request_necessary_equipment", on_delete=models.CASCADE)
    objects = models.Manager()  

    class Meta:
        db_table = "tbl_meeting_request"