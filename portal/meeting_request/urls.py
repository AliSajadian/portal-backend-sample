from rest_framework import routers

from .views import Meeting_Cater_TypeViewSet, Meeting_Necessary_EquipmentViewSet, Meeting_RequestViewSet


router = routers.DefaultRouter()
router.register('api/meetingcatertype', Meeting_Cater_TypeViewSet, 'meetingcatertype')
router.register('api/meetingnecessaryequipment', Meeting_Necessary_EquipmentViewSet, 'meetingnecessaryequipment')
router.register('api/meetingrequest', Meeting_RequestViewSet, 'meetingrequest')

urlpatterns = router.urls
