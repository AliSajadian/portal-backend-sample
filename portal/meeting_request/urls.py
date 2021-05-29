from django.urls import path
from rest_framework import routers

from .views import Meeting_RoomViewSet, Meeting_Room_TypeViewSet, Meeting_RequestViewSet, \
    Meeting_Cater_TypeViewSet, Meeting_EquipmentViewSet, Meeting_DateRequestsAPI, \
    GetRequest_Cater_TypesAPI, PutRequest_Cater_TypesAPI


router = routers.DefaultRouter()
router.register('api/roomtypes', Meeting_Room_TypeViewSet, 'roomtypes')
router.register('api/rooms', Meeting_RoomViewSet, 'rooms')
router.register('api/catertypes', Meeting_Cater_TypeViewSet, 'catertypes')
router.register('api/equipments', Meeting_EquipmentViewSet, 'equipments')
router.register('api/requests', Meeting_RequestViewSet, 'requests')

urlpatterns = [
    path("api/daterequests/<str:date>", Meeting_DateRequestsAPI.as_view(), name="daterequests/<date>"),
    path('api/requestcatertypes/<str:date>', GetRequest_Cater_TypesAPI.as_view(), name="requestcatertypes/<date>"),
    path('api/requestcatertype/<int:pk>', PutRequest_Cater_TypesAPI.as_view(), name="requestcatertype/<pk>/"),
]

urlpatterns += router.urls
