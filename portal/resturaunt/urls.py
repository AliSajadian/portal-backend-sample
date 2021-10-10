from django.urls import path, re_path
from rest_framework import routers

from .views import Resturaunt_MealViewSet, Resturaunt_Day_Meal_Current_MonthViewSet, Resturaunt_Day_Meal_Next_MonthViewSet, Resturaunt_Day_MealViewSet, \
        Resturaunt_Day_MealExViewSet, Resturaunt_Day_Meal_ActivationViewSet, Resturaunt_Employee_Day_MealViewSet, Resturaunt_Employee_Day_Meal_Current_MonthViewSet, \
        Resturaunt_Employee_OneDay_MealViewSet, Resturaunt_Fish_MealViewSet, Resturaunt_Department_Day_MealsAPI, Resturaunt_Project_Day_MealsAPI, \
        Resturaunt_Served_MealViewSet, Restrant_Set_ServedViewSet , Resturaunt_Edit_Guest_Day_MealsViewSet, Resturaunt_Employee_Day_Meal_Next_MonthViewSet, \
        Resturaunt_Guest_Day_MealViewSet, Resturaunt_Edit_Guest_Day_MealsJunction, Resturaunt_DepartmentsMealsDailyListViewSet, Resturaunt_ProjectsMealsDailyListViewSet, \
        Resturaunt_SectionsMealsDailyListViewSet, Resturaunt_Department_Guest_Day_MealsViewSet, Resturaunt_Project_Guest_Day_MealsViewSet, Resturaunt_Section_NameViewSet, \
        Resturaunt_CurrentMonthSelectedMealsViewSet, Resturaunt_AsftDayMealsStatisticsViewSet, Resturaunt_CompanysDayMealsStatisticsViewSet, \
        Resturaunt_SectionDayMealsStatisticsViewSet, Resturaunt_DepartmentDayMealsStatisticsViewSet, Resturaunt_ProjectDayMealsStatisticsViewSet, \
        Resturaunt_MealsStatisticsDatesListViewSet, Resturaunt_ContractorMonthlyMealsStatisticsViewSet, Resturaunt_Save_Current_Month_Employee_Meal_Day, \
        Resturaunt_Save_Next_Month_Employee_Meal_Day, Resturaunt_Contractor_Daily_Section_Meals_StatisticsViewAPI, Resturaunt_Day_Meals_NamesViewAPI, \
        Resturaunt_Day_Meals_TotalNoViewAPI, Resturaunt_Personel_Didnot_Select_Next_Month_MealsViewAPI, Resturaunt_Section_NamesViewAPI


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
    path('api/sectionsmealsdailylist/<int:employeeId>/', Resturaunt_SectionsMealsDailyListViewSet.as_view(), name='sectionsmealsdailylist/<employeeId>/'),
    path('api/sectionname/<int:employeeId>/', Resturaunt_Section_NameViewSet.as_view(), name='sectionname/<employeeId>/'),

    path('api/currentmonthselectedmeals/<int:employeeId>/', Resturaunt_CurrentMonthSelectedMealsViewSet.as_view(), name='currentmonthselectedmeals/<employeeId>/'),    
    re_path(r'api/asftdaymealsstatistics/(?P<date>\d{4}-\d{2}-\d{2})$', Resturaunt_AsftDayMealsStatisticsViewSet.as_view()),    
    re_path(r'^api/companysdaymealsstatistics/(?P<date>\d{4}-\d{2}-\d{2})$', Resturaunt_CompanysDayMealsStatisticsViewSet.as_view()), 
    path('api/sectiondaymealsstatistics/<int:employeeId>/', Resturaunt_SectionDayMealsStatisticsViewSet.as_view(), name='sectiondaymealsstatistics/<employeeId>/'),    
    path('api/departmentdaymealsstatistics/<int:departmentId>/', Resturaunt_DepartmentDayMealsStatisticsViewSet.as_view(), name='departmentdaymealsstatistics/<departmentId>/'),    
    path('api/projectdaymealsstatistics/<int:projectId>/', Resturaunt_ProjectDayMealsStatisticsViewSet.as_view(), name='projectdaymealsstatistics/<projectId>/'),    
    path('api/contractormonthlymealsstatistics/', Resturaunt_ContractorMonthlyMealsStatisticsViewSet.as_view(), name='contractormonthlymealsstatistics/'),   
    path('api/mealsstatisticsdateslist/', Resturaunt_MealsStatisticsDatesListViewSet.as_view(), name='mealsstatisticsdateslist/'),
    path('api/savebulkcurrentmonthpersonelmealdays', Resturaunt_Save_Current_Month_Employee_Meal_Day.as_view(), name='savebulkcurrentmonthpersonelmealdays'),
    path('api/savebulknextmonthpersonelmealdays', Resturaunt_Save_Next_Month_Employee_Meal_Day.as_view(), name='savebulknextmonthpersonelmealdays'),
    path('api/contractorsectionsdailymealsstatistics/', Resturaunt_Contractor_Daily_Section_Meals_StatisticsViewAPI.as_view(), name='api/contractorsectionsdailymealsstatistics/'),
    path('api/todaymealsnames/', Resturaunt_Day_Meals_NamesViewAPI.as_view(), name='api/todaymealsnames/'),
    path('api/todaymealstotalno/', Resturaunt_Day_Meals_TotalNoViewAPI.as_view(), name='api/todaymealstotalno/'),
    path('api/personelwhodidnotselectnextmonthmeals/', Resturaunt_Personel_Didnot_Select_Next_Month_MealsViewAPI.as_view(), name='api/personelwhodidnotselectnextmonthmeals/'),
    path('api/sectionnames/', Resturaunt_Section_NamesViewAPI.as_view(), name='api/sectionnames'),
]

urlpatterns += router.urls
