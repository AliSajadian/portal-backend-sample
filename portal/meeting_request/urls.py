from django.urls import path
from rest_framework import routers

from .views import Meeting_RoomViewSet, Meeting_Room_TypeViewSet, Meeting_RequestViewSet, \
    Meeting_Cater_TypeViewSet, Meeting_EquipmentViewSet, Meeting_DateRequestsAPI, \
    GetRequest_Cater_TypesAPI, GetRequest_EquipmentsAPI, PutRequest_Cater_TypesAPI, \
    Meeting_Room_EquipmentAPI, Meeting_Request_Cater_TypeViewSet, SaveMeeting_RequestAPI
    


router = routers.DefaultRouter()
router.register('api/roomtypes', Meeting_Room_TypeViewSet, 'roomtypes')
router.register('api/rooms', Meeting_RoomViewSet, 'rooms')
router.register('api/catertypes', Meeting_Cater_TypeViewSet, 'catertypes')
router.register('api/equipments', Meeting_EquipmentViewSet, 'equipments')
router.register('api/requests', Meeting_RequestViewSet, 'requests')
router.register('api/requestscatertypes', Meeting_Request_Cater_TypeViewSet, 'requestscatertypes')

urlpatterns = [
    path("api/daterequests", Meeting_DateRequestsAPI.as_view(), name="daterequests"),
    path('api/requestcatertypesex/<int:id>', GetRequest_Cater_TypesAPI.as_view(), name="requestcatertypesex/<int>"),
    path('api/requestequipmentsex/<int:id>', GetRequest_EquipmentsAPI.as_view(), name="requestequipmentsex/<int>"),
    path('api/requestcatertype/<int:pk>', PutRequest_Cater_TypesAPI.as_view(), name="requestcatertype/<pk>/"),
    path('api/roomfixedequipments/<int:id>', Meeting_Room_EquipmentAPI.as_view(), name="roomfixedequipments/<id>/"),
    path('api/saverequest', SaveMeeting_RequestAPI.as_view(), name="saverequest"),
]

urlpatterns += router.urls
