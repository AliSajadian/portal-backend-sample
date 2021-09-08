from django.urls import path, re_path
from rest_framework import routers

from .views import Resturaunt_MealViewSet, Resturaunt_Day_Meal_Current_MonthViewSet, Resturaunt_Day_Meal_Next_MonthViewSet, Resturaunt_Day_MealViewSet, \
        Resturaunt_Day_MealExViewSet, Resturaunt_Day_Meal_ActivationViewSet, Resturaunt_Employee_Day_MealViewSet, Resturaunt_Employee_Day_Meal_Current_MonthViewSet, \
        Resturaunt_Employee_OneDay_MealViewSet, Resturaunt_Fish_MealViewSet, Resturaunt_Department_Day_MealsAPI, Resturaunt_Project_Day_MealsAPI, \
        Resturaunt_Served_MealViewSet, Restrant_Set_ServedViewSet , Resturaunt_Edit_Guest_Day_MealsViewSet, Resturaunt_Employee_Day_Meal_Next_MonthViewSet, \
        Resturaunt_Guest_Day_MealViewSet, Resturaunt_Edit_Guest_Day_MealsJunction, Resturaunt_DepartmentsMealsDailyListViewSet, \
        Resturaunt_ProjectsMealsDailyListViewSet, Resturaunt_Department_Guest_Day_MealsViewSet, Resturaunt_Project_Guest_Day_MealsViewSet, \
        Resturaunt_CurrentMonthSelectedMealsViewSet, Resturaunt_AsftDayMealsStatisticsViewSet, Resturaunt_CompanysDayMealsStatisticsViewSet, \
        Resturaunt_ContractorMonthlyMealsStatisticsViewSet, Resturaunt_Save_Employee_Meal_Day


router = routers.DefaultRouter()
router.register('api/meals', Resturaunt_MealViewSet, 'meals')

router.register('api/mealdays', Resturaunt_Day_MealViewSet, 'mealdays')
router.register('api/mealdayscurrentmonth', Resturaunt_Day_Meal_Current_MonthViewSet, 'mealdayscurrentmonth')
router.register('api/mealdaysnextmonth', Resturaunt_Day_Meal_Next_MonthViewSet, 'mealdaysnextmonth')

router.register('api/personelmealdays', Resturaunt_Employee_Day_MealViewSet, 'personelmealdays')
router.register('api/personelmealsoneday', Resturaunt_Employee_OneDay_MealViewSet, 'personelmealsoneday')
router.register('api/personelmealdayscurrentmonth/(?P<employee_id>\d+)', Resturaunt_Employee_Day_Meal_Current_MonthViewSet, 'personelmealdayscurrentmonth'),
router.register('api/personelmealdaysnextmonth/(?P<employee_id>\d+)', Resturaunt_Employee_Day_Meal_Next_MonthViewSet, 'personelmealdaysnextmonth'),

router.register('api/servedmeals', Resturaunt_Served_MealViewSet, 'servedmeals')
# router.register('api/fishmeal/(?P<code>\d+)', Resturaunt_Fish_MealViewSet, 'fishmeal')
router.register('api/guestmealsdays', Resturaunt_Guest_Day_MealViewSet, 'guestmealsdays')

urlpatterns = [
    path("api/fishmeal/<int:code>/", Resturaunt_Fish_MealViewSet.as_view(), name="fishmeal/<code>/"),
    path("api/servemeal/<int:id>/", Restrant_Set_ServedViewSet.as_view(), name="servemeal/<id>/"),

    re_path(r'^api/mealdaysex/(?P<date>\d{4}-\d{2}-\d{2})$', Resturaunt_Day_MealExViewSet.as_view()),
    re_path(r'^api/activatepersonelmealdayselection/(?P<date>\d{4}-\d{2}-\d{2})$', Resturaunt_Day_Meal_ActivationViewSet.as_view()),
    
    path('api/departmentmealsday/<str:selectedDate>/<int:departmentId>', Resturaunt_Department_Day_MealsAPI.as_view(), name='departmentmealsday/<selectedDate>/<departmentId>'),
    path('api/projectmealsday/<str:selectedDate>/<int:projectId>', Resturaunt_Project_Day_MealsAPI.as_view(), name='projectmealsday/<selectedDate>/<projectId>'),
    path('api/departmentguestsmealsdaylist/<str:selectedDate>/<int:departmentId>/', Resturaunt_Department_Guest_Day_MealsViewSet.as_view(), name='departmentguestsmealsdaylist/<selectedDate>/<departmentId>/'),
    path('api/projectguestsmealsdaylist/<str:selectedDate>/<int:projectId>/', Resturaunt_Project_Guest_Day_MealsViewSet.as_view(), name='projectguestsmealsdaylist/<selectedDate>/<projectId>/'),
    # path('api/projectguestmealsday/<str:selectedDate>/<int:projectId>', Resturaunt_Project_Guest_Day_MealsViewSet.as_view(), name='projectguestmealsday/<selectedDate>/<projectId>'),
    path('api/guestmealsday/', Resturaunt_Edit_Guest_Day_MealsViewSet.as_view(), name='guestmealsday/'),
    path("api/guestmealdayjunction/", Resturaunt_Edit_Guest_Day_MealsJunction.as_view(), name="guestmealdayjunction/"),

    path('api/departmentsmealsdailylist/<int:departmentId>/', Resturaunt_DepartmentsMealsDailyListViewSet.as_view(), name='departmentsmealsdailylist/<departmentId>/'),
    path('api/projectsmealsdailylist/<int:projectId>/', Resturaunt_ProjectsMealsDailyListViewSet.as_view(), name='projectsmealsdailylist/<projectId>/'),

    path('api/currentmonthselectedmeals/<int:employeeId>/', Resturaunt_CurrentMonthSelectedMealsViewSet.as_view(), name='currentmonthselectedmeals/<employeeId>/'),    
    re_path(r'api/asftdaymealsstatistics/(?P<date>\d{4}-\d{2}-\d{2})$', Resturaunt_AsftDayMealsStatisticsViewSet.as_view()),    
    re_path(r'^api/companysdaymealsstatistics/(?P<date>\d{4}-\d{2}-\d{2})$', Resturaunt_CompanysDayMealsStatisticsViewSet.as_view()), 
    path('api/contractormonthlymealsstatistics/', Resturaunt_ContractorMonthlyMealsStatisticsViewSet.as_view(), name='contractormonthlymealsstatistics/'),   
    path('api/savebulkpersonelmealdays', Resturaunt_Save_Employee_Meal_Day.as_view(), name='savebulkpersonelmealdays')
]

urlpatterns += router.urls
