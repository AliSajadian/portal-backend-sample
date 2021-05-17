from rest_framework import routers

from .views import Meeting_RoomViewSet, \
    Meeting_RequestViewSet, Meeting_Cater_TypeViewSet, Meeting_EquipmentViewSet


router = routers.DefaultRouter()
router.register('api/rooms', Meeting_RoomViewSet, 'rooms')
router.register('api/catertypes', Meeting_Cater_TypeViewSet, 'catertypes')
router.register('api/equipments', Meeting_EquipmentViewSet, 'equipments')
router.register('api/requests', Meeting_RequestViewSet, 'requests')

urlpatterns = router.urls
