from rest_framework import routers

from .views import DoctorsViewSet, DocPatientsViewSet, DocPatientsFilesViewSet, PatientsFileUploadViewSet, \
    DocSchedulesWeekDaysViewSet, DocSchedulesDaysViewSet, DocAppointmentTimesViewSet, FilteredAppointmentTimesViewSet, \
        DocAppointmentsViewSet


router = routers.DefaultRouter()
router.register('api/doctors', DoctorsViewSet, 'doctors')
router.register('api/doctorpatients', DocPatientsViewSet, 'doctorpatients')
router.register('api/patientsfileupload', PatientsFileUploadViewSet, 'patientsfileupload')
router.register('api/doctorpatientsfiles', DocPatientsFilesViewSet, 'doctorpatientsfiles')
router.register('api/filteredappointmenttimes/(?P<id>\d+)', FilteredAppointmentTimesViewSet, 'filteredappointmenttimes/')
router.register('api/scheduleweeklydays', DocSchedulesWeekDaysViewSet, 'scheduleweeklydays')
router.register('api/scheduledays', DocSchedulesDaysViewSet, 'scheduledays')
router.register('api/appointmenttimes', DocAppointmentTimesViewSet, 'appointmenttimes')
router.register('api/appointments', DocAppointmentsViewSet, 'appointments')

urlpatterns = router.urls