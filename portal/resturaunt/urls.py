from django.urls import path
from rest_framework import routers

from .views import Resturaunt_MealViewSet, Resturaunt_Day_MealViewSet, Resturaunt_Day_MealExViewSet, Resturaunt_Employee_Day_MealViewSet, \
        Resturaunt_Employee_Day_MealExViewSet, Resturaunt_Employee_OneDay_MealViewSet, Resturaunt_Served_MealViewSet, \
        Resturaunt_Fish_MealViewSet, Resturaunt_Get_Day_MealsAPI, Resturaunt_Employee_Day_MealExViewSet, \
        Restrant_Set_ServedViewSet , Resturaunt_Get_Guest_Day_MealsViewSet, Resturaunt_Edit_Guest_Day_MealsViewSet, \
        Resturaunt_Guest_Day_MealViewSet, Resturaunt_Edit_Guest_Day_MealsJunction


router = routers.DefaultRouter()
router.register('api/meals', Resturaunt_MealViewSet, 'meals')

router.register('api/mealdays', Resturaunt_Day_MealViewSet, 'mealdays')
router.register('api/mealdaysex', Resturaunt_Day_MealExViewSet, 'mealdaysex')

router.register('api/personelmealdays', Resturaunt_Employee_Day_MealViewSet, 'personelmealdays')
router.register('api/personelmealdaysex/(?P<employee_id>\d+)', Resturaunt_Employee_Day_MealExViewSet, 'personelmealdaysex/')
router.register('api/personelmealsoneday', Resturaunt_Employee_OneDay_MealViewSet, 'personelmealsoneday')

router.register('api/servedmeals', Resturaunt_Served_MealViewSet, 'servedmeals')
# router.register('api/fishmeal/(?P<code>\d+)', Resturaunt_Fish_MealViewSet, 'fishmeal')
router.register('api/guestmealsdays', Resturaunt_Guest_Day_MealViewSet, 'guestmealsdays')

urlpatterns = [
    path("api/fishmeal/<int:code>/", Resturaunt_Fish_MealViewSet.as_view(), name="fishmeal/<code>/"),
    path("api/servemeal/<int:id>/", Restrant_Set_ServedViewSet.as_view(), name="servemeal/<id>/"),
    
    path('api/mealsday/<str:selectedDate>/<int:departmentId>', Resturaunt_Get_Day_MealsAPI.as_view(), name='mealsday/<selectedDate>/<departmentId>'),
    path('api/guestmealsday/<str:selectedDate>/<int:departmentId>', Resturaunt_Get_Guest_Day_MealsViewSet.as_view(), name='guestmealsday/<selectedDate>/<departmentId>'),
    path('api/guestmealsday/', Resturaunt_Edit_Guest_Day_MealsViewSet.as_view(), name='guestmealsday/'),
    path("api/guestmealdayjunction/", Resturaunt_Edit_Guest_Day_MealsJunction.as_view(), name="guestmealdayjunction/"),
]

urlpatterns += router.urls
