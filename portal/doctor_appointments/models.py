from django.db import models
from datetime import datetime

from django.contrib.auth.models import User
from baseInfo.models import DoctorType, Employee



class Doctors(models.Model):
    visitDuration = models.PositiveSmallIntegerField(null=True)
    employee = models.ForeignKey(Employee, 
        related_name="Employee_Doctor", on_delete=models.CASCADE, null=True)
    doctorType = models.ForeignKey(DoctorType,
        related_name="DoctorType_Doctor", on_delete=models.CASCADE, null=True)
    objects = models.Manager()

    class Meta:
        db_table = "tbl_doctors"


class DocPatients(models.Model):
    doctor = models.ForeignKey(Doctors,
         related_name="Doctors_Patient", on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee,
         related_name="Employees_Patient", on_delete=models.CASCADE, null=True)
    objects = models.Manager()

    class Meta:
        db_table = "tbl_doc_patients"   


class DocSchedulesWeekDays(models.Model):
    doctor = models.ForeignKey(Doctors,
        related_name="Doctor_ScheduleWeekDays", on_delete=models.CASCADE, null=True)
    week_day = models.PositiveSmallIntegerField()
    start_hour= models.TimeField(auto_now=False, auto_now_add=False)
    end_hour = models.TimeField(auto_now=False, auto_now_add=False)
    objects = models.Manager()

    class Meta:
        db_table = "tbl_doc_schedule_weekdays"


class DocSchedulesDays(models.Model):
    schedulesWeekDay = models.ForeignKey(DocSchedulesWeekDays,
        related_name="ScheduleWeekDay_ScheduleDays", on_delete=models.CASCADE, null=True)
    date = models.DateField(default=datetime.now, blank=True)
    start_hour= models.TimeField(auto_now=False, auto_now_add=False)
    end_hour = models.TimeField(auto_now=False, auto_now_add=False)
    visitDuration = models.PositiveSmallIntegerField()
    objects = models.Manager()

    class Meta:
        db_table = "tbl_doc_schedule_days"


class DocAppointmentTimes(models.Model):
    schedulesDay = models.ForeignKey(DocSchedulesDays,
        related_name="Scheduleday_Appointmenttime", on_delete=models.CASCADE, null=True)
    reserveNo = models.PositiveSmallIntegerField()
    reserveTime = models.TimeField(auto_now=False, auto_now_add=False)
    objects = models.Manager()
    
    class Meta:
        db_table = "tbl_doc_appointment_times"   


class DocAppointments(models.Model):
    doctor = models.ForeignKey(Doctors,
        related_name="Doctor_Appointment", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User,
        related_name="User_Appointment", on_delete=models.CASCADE, null=True)
    # patient = models.ForeignKey(DocPatients,
    #     related_name="patient_appointment", on_delete=models.CASCADE, null=True)
    appointmentTime = models.ForeignKey(DocAppointmentTimes,
        related_name="Appointmenttime_Appointment", on_delete=models.CASCADE, null=True)   
    description = models.CharField(max_length=500, blank=True, null=True)
    canceled = models.BooleanField(default=False)
    passed = models.BooleanField(default=False)
    used = models.BooleanField(default=False)
    objects = models.Manager()
    
    class Meta:
        db_table = "tbl_doc_appointments"        


class PatientsFileDownloadManager(models.Manager):
    def get_patientfiledownload(self, patientFileID):
        from django.db import connection
        from collections import defaultdict

        # userID = HttpRequest["userID"]
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT pf.id, pf.file , pf.appointment_id, pf.fileTitle
                FROM tbl_doc_patients_files pf
                WHERE pf.id  = %s''', [patientFileID])
                # %s ''', (userID,)) id = row[0], s.id, 

            result_list = []
            for row in cursor.fetchall():
                s = self.model(id = row[0], file = row[1], appointment_id = row[2], fileTitle = row[3])
                result_list.append(s)

            return result_list


class DocPatientsFiles(models.Model):
    fileTitle = models.CharField(max_length=150, blank=True)
    file = models.FileField(upload_to='patient_files', null=True)
    appointment = models.ForeignKey(DocAppointments,
         related_name="Appointment_PatientFile", on_delete=models.CASCADE, null=True)
    objects = models.Manager()
    patientfile_download_objects = PatientsFileDownloadManager()

    class Meta:
        db_table = "tbl_doc_patients_files"  
