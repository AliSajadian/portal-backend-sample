from django.db.models.expressions import ExpressionList
from django.http import response
from django.db.models import Count, Q, F, Window, Value, IntegerField
from django.db.models.functions import RowNumber
from datetime import date, datetime ,timedelta
from django.db.models import Count, Value, CharField, SmallIntegerField
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response 
from django_pivot.pivot import pivot

from baseInfo.models import Employee, Department, Project
from resturaunt.models import Resturaunt_Meal, Resturaunt_Day_Meal, Resturaunt_Employee_Day_Meal, Resturaunt_Guest_Day_Meal_Junction, Resturaunt_Guest_Day_Meal
from .serializers import Resturaunt_MealSerializer, Resturaunt_Day_MealSerializer, Resturaunt_Day_MealExSerializer, Resturaunt_Served_MealSerializer, \
        Resturaunt_Fish_MealSerializer, Resturaunt_Employee_Day_MealSerializer, Resturaunt_Employee_Day_MealProSerializer, Resturaunt_Employee_Day_MealExSerializer, \
        Resturaunt_Guest_Day_MealSerializer, Resturaunt_Guest_Day_MealExSerializer


class Resturaunt_MealViewSet(viewsets.ModelViewSet):
    queryset = Resturaunt_Meal.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Resturaunt_MealSerializer


class Resturaunt_Day_MealViewSet(viewsets.ModelViewSet):
    queryset = Resturaunt_Day_Meal.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Resturaunt_Day_MealSerializer

class Resturaunt_Day_Meal_Current_MonthViewSet(viewsets.ModelViewSet):
    # queryset = Resturaunt_Day_Meal.objects.all()

    permission_classes = [permissions.IsAuthenticated] 

    serializer_class = Resturaunt_Day_MealSerializer

    def get_queryset(self):
        currentdate = date.today()
        y = currentdate.year
        m = currentdate.month-1
        d = currentdate.day
        startdate = ""
        enddate = ""
        if(m == 1):
            startdate += str(y) 
            startdate += "-01" if (d < 21) else "-02" 
            startdate += "-21" if (d < 21) else "-20"
            enddate += str(y) 
            enddate += "-02" if (d < 21) else "-03" 
            enddate += "-19" if (d < 21) else "-20"
        elif(m == 2):
            startdate += str(y) 
            startdate += "-02" if (d < 20) else "-03" 
            startdate += "-20" if (d < 20) else "-21"
            enddate += str(y) 
            enddate += "-03" if (d < 20) else "-04" 
            enddate += "-20" if (d < 20) else "-20"
        elif(m == 3):
            startdate += str(y) 
            startdate += "-03" if (d < 21) else "-04" 
            startdate += "-21" if (d < 21) else "-21"
            enddate += str(y) 
            enddate += "-04" if (d < 21) else "-05" 
            enddate += "-21" if (d < 21) else "-21"
        elif(m == 4):
            startdate += str(y) 
            startdate += "-04" if (d < 21) else "-05" 
            startdate += "-21" if (d < 21) else "-22"
            enddate += str(y) 
            enddate += "-05" if (d < 21) else "-06" 
            enddate += "-21" if (d < 21) else "-21"            
        elif(m == 5):
            startdate += str(y) 
            startdate += "-05" if (d < 22) else "-06" 
            startdate += "-22" if (d < 22) else "-22" 
            enddate += str(y) 
            enddate += "-06" if (d < 22) else "-07" 
            enddate += "-21" if (d < 22) else "-22"            
        elif(m == 6):
            startdate += str(y) 
            startdate += "-06" if (d < 22) else "-07" 
            startdate += "-22" if (d < 22) else "-23" 
            enddate += str(y) 
            enddate += "-07" if (d < 22) else "-08" 
            enddate += "-22" if (d < 22) else "-22"            
        elif(m == 7):
            startdate += str(y) 
            startdate += "-07" if (d < 23) else "-08" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-08" if (d < 23) else "-09" 
            enddate += "-22" if (d < 23) else "-22"            
        elif(m == 8):
            startdate += str(y) 
            startdate += "-08" if (d < 23) else "-09" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-09" if (d < 23) else "-10" 
            enddate += "-22" if (d < 23) else "-22"
        elif(m == 9):
            startdate = str(y) 
            startdate += "-09" if (d < 23) else "-10" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-10" if (d < 23) else "-11" 
            enddate += "-22" if (d < 23) else "-21"            
        elif(m == 10):
            startdate += str(y) 
            startdate += "-10" if (d < 23) else "-11" 
            startdate += "-23" if (d < 23) else "-22" 
            enddate += str(y) 
            enddate += "-11" if (d < 23) else "-12" 
            enddate += "-21" if (d < 23) else "-21"            
        elif(m == 11):
            startdate += str(y) 
            startdate += "-11" if (d < 22) else "-12" 
            startdate += "-22" if (d < 22) else "-22" 
            enddate += str(y) 
            enddate += "-12" if (d < 22) else "-01" 
            enddate += "-21" if (d < 22) else "-20"
        elif(m == 12):
            startdate += str(y) 
            startdate += "-12" if (d < 22) else "-01" 
            startdate += "-22" if (d < 22) else "-21"
            enddate += str(y) 
            enddate += "-01" if (d < 22) else "-02" 
            enddate += "-20" if (d < 22) else "-19"             

        return Resturaunt_Day_Meal.objects.filter(date__gte=startdate, date__lte=enddate, isActive__exact=False)

class Resturaunt_Day_Meal_Next_MonthViewSet(viewsets.ModelViewSet):
    # queryset = Resturaunt_Day_Meal.objects.all()

    permission_classes = [permissions.IsAuthenticated] 

    serializer_class = Resturaunt_Day_MealSerializer

    def get_queryset(self):
        currentdate = date.today()
        y = currentdate.year
        m = currentdate.month
        d = currentdate.day
        startdate = ""
        enddate = ""
        if(m == 1):
            startdate += str(y) 
            startdate += "-01" if (d < 21) else "-02" 
            startdate += "-21" if (d < 21) else "-20"
            enddate += str(y) 
            enddate += "-02" if (d < 21) else "-03" 
            enddate += "-19" if (d < 21) else "-20"
        elif(m == 2):
            startdate += str(y) 
            startdate += "-02" if (d < 20) else "-03" 
            startdate += "-20" if (d < 20) else "-21"
            enddate += str(y) 
            enddate += "-03" if (d < 20) else "-04" 
            enddate += "-20" if (d < 20) else "-20"
        elif(m == 3):
            startdate += str(y) 
            startdate += "-03" if (d < 21) else "-04" 
            startdate += "-21" if (d < 21) else "-21"
            enddate += str(y) 
            enddate += "-04" if (d < 21) else "-05" 
            enddate += "-21" if (d < 21) else "-21"
        elif(m == 4):
            startdate += str(y) 
            startdate += "-04" if (d < 21) else "-05" 
            startdate += "-21" if (d < 21) else "-22"
            enddate += str(y) 
            enddate += "-05" if (d < 21) else "-06" 
            enddate += "-21" if (d < 21) else "-21"            
        elif(m == 5):
            startdate += str(y) 
            startdate += "-05" if (d < 22) else "-06" 
            startdate += "-22" if (d < 22) else "-22" 
            enddate += str(y) 
            enddate += "-06" if (d < 22) else "-07" 
            enddate += "-21" if (d < 22) else "-22"            
        elif(m == 6):
            startdate += str(y) 
            startdate += "-06" if (d < 22) else "-07" 
            startdate += "-22" if (d < 22) else "-23" 
            enddate += str(y) 
            enddate += "-07" if (d < 22) else "-08" 
            enddate += "-22" if (d < 22) else "-22"            
        elif(m == 7):
            startdate += str(y) 
            startdate += "-07" if (d < 23) else "-08" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-08" if (d < 23) else "-09" 
            enddate += "-22" if (d < 23) else "-22"            
        elif(m == 8):
            startdate += str(y) 
            startdate += "-08" if (d < 23) else "-09" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-09" if (d < 23) else "-10" 
            enddate += "-22" if (d < 23) else "-22"
        elif(m == 9):
            startdate = str(y) 
            startdate += "-09" if (d < 23) else "-10" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-10" if (d < 23) else "-11" 
            enddate += "-22" if (d < 23) else "-21"            
        elif(m == 10):
            startdate += str(y) 
            startdate += "-10" if (d < 23) else "-11" 
            startdate += "-23" if (d < 23) else "-22" 
            enddate += str(y) 
            enddate += "-11" if (d < 23) else "-12" 
            enddate += "-21" if (d < 23) else "-21"            
        elif(m == 11):
            startdate += str(y) 
            startdate += "-11" if (d < 22) else "-12" 
            startdate += "-22" if (d < 22) else "-22" 
            enddate += str(y) 
            enddate += "-12" if (d < 22) else "-01" 
            enddate += "-21" if (d < 22) else "-20"
        elif(m == 12):
            startdate += str(y) 
            startdate += "-12" if (d < 22) else "-01" 
            startdate += "-22" if (d < 22) else "-21"
            enddate += str(y) 
            enddate += "-01" if (d < 22) else "-02" 
            enddate += "-20" if (d < 22) else "-19"             
            
        return Resturaunt_Day_Meal.objects.filter(date__gte=startdate, date__lte=enddate, isActive__exact=False)

class Resturaunt_Day_MealExViewSet(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated] 

    def get(self, request, *args, **kwargs):
        date = self.kwargs['date']
        currentdate = datetime.strptime(date, '%Y-%m-%d').date()

        y = currentdate.year
        m = currentdate.month-1
        d = currentdate.day
        startdate = ""
        enddate = ""
        if(m == 1):
            startdate += str(y) 
            startdate += "-01" if (d < 21) else "-02" 
            startdate += "-21" if (d < 21) else "-20"
            enddate += str(y) 
            enddate += "-02" if (d < 21) else "-03" 
            enddate += "-19" if (d < 21) else "-20"
        elif(m == 2):
            startdate += str(y) 
            startdate += "-02" if (d < 20) else "-03" 
            startdate += "-20" if (d < 20) else "-21"
            enddate += str(y) 
            enddate += "-03" if (d < 20) else "-04" 
            enddate += "-20" if (d < 20) else "-20"
        elif(m == 3):
            startdate += str(y) 
            startdate += "-03" if (d < 21) else "-04" 
            startdate += "-21" if (d < 21) else "-21"
            enddate += str(y) 
            enddate += "-04" if (d < 21) else "-05" 
            enddate += "-21" if (d < 21) else "-21"
        elif(m == 4):
            startdate += str(y) 
            startdate += "-04" if (d < 21) else "-05" 
            startdate += "-21" if (d < 21) else "-22"
            enddate += str(y) 
            enddate += "-05" if (d < 21) else "-06" 
            enddate += "-21" if (d < 21) else "-21"            
        elif(m == 5):
            startdate += str(y) 
            startdate += "-05" if (d < 22) else "-06" 
            startdate += "-22" if (d < 22) else "-22" 
            enddate += str(y) 
            enddate += "-06" if (d < 22) else "-07" 
            enddate += "-21" if (d < 22) else "-22"            
        elif(m == 6):
            startdate += str(y) 
            startdate += "-06" if (d < 22) else "-07" 
            startdate += "-22" if (d < 22) else "-23" 
            enddate += str(y) 
            enddate += "-07" if (d < 22) else "-08" 
            enddate += "-22" if (d < 22) else "-22"            
        elif(m == 7):
            startdate += str(y) 
            startdate += "-07" if (d < 23) else "-08" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-08" if (d < 23) else "-09" 
            enddate += "-22" if (d < 23) else "-22"            
        elif(m == 8):
            startdate += str(y) 
            startdate += "-08" if (d < 23) else "-09" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-09" if (d < 23) else "-10" 
            enddate += "-22" if (d < 23) else "-22"
        elif(m == 9):
            startdate = str(y) 
            startdate += "-09" if (d < 23) else "-10" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-10" if (d < 23) else "-11" 
            enddate += "-22" if (d < 23) else "-21"            
        elif(m == 10):
            startdate += str(y) 
            startdate += "-10" if (d < 23) else "-11" 
            startdate += "-23" if (d < 23) else "-22" 
            enddate += str(y) 
            enddate += "-11" if (d < 23) else "-12" 
            enddate += "-21" if (d < 23) else "-21"            
        elif(m == 11):
            startdate += str(y) 
            startdate += "-11" if (d < 22) else "-12" 
            startdate += "-22" if (d < 22) else "-22" 
            enddate += str(y) 
            enddate += "-12" if (d < 22) else "-01" 
            enddate += "-21" if (d < 22) else "-20"
        elif(m == 12):
            startdate += str(y) 
            startdate += "-12" if (d < 22) else "-01" 
            startdate += "-22" if (d < 22) else "-21"
            enddate += str(y) 
            enddate += "-01" if (d < 22) else "-02" 
            enddate += "-20" if (d < 22) else "-19"             


        results = Resturaunt_Day_Meal.objects.filter(date__gte=startdate, date__lte=enddate).annotate(
            selectedNo=Count('ResturauntDayMeal_ResturauntEmployeeDayMeal')).values('id', 'date', 'totalNo', 'isActive', 'resturaunt_meal', 'selectedNo')
        return Response(results)    

class Resturaunt_Day_Meal_ActivationViewSet(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated] 

    def get(self, request, *args, **kwargs):
        date = self.kwargs['date']
        currentdate = datetime.strptime(date, '%Y-%m-%d').date()

        y = currentdate.year
        m = currentdate.month-1
        d = currentdate.day
        startdate = ""
        enddate = ""
        if(m == 1):
            startdate += str(y) 
            startdate += "-01" if (d < 21) else "-02" 
            startdate += "-21" if (d < 21) else "-20"
            enddate += str(y) 
            enddate += "-02" if (d < 21) else "-03" 
            enddate += "-19" if (d < 21) else "-20"
        elif(m == 2):
            startdate += str(y) 
            startdate += "-02" if (d < 20) else "-03" 
            startdate += "-20" if (d < 20) else "-21"
            enddate += str(y) 
            enddate += "-03" if (d < 20) else "-04" 
            enddate += "-20" if (d < 20) else "-20"
        elif(m == 3):
            startdate += str(y) 
            startdate += "-03" if (d < 21) else "-04" 
            startdate += "-21" if (d < 21) else "-21"
            enddate += str(y) 
            enddate += "-04" if (d < 21) else "-05" 
            enddate += "-21" if (d < 21) else "-21"
        elif(m == 4):
            startdate += str(y) 
            startdate += "-04" if (d < 21) else "-05" 
            startdate += "-21" if (d < 21) else "-22"
            enddate += str(y) 
            enddate += "-05" if (d < 21) else "-06" 
            enddate += "-21" if (d < 21) else "-21"            
        elif(m == 5):
            startdate += str(y) 
            startdate += "-05" if (d < 22) else "-06" 
            startdate += "-22" if (d < 22) else "-22" 
            enddate += str(y) 
            enddate += "-06" if (d < 22) else "-07" 
            enddate += "-21" if (d < 22) else "-22"            
        elif(m == 6):
            startdate += str(y) 
            startdate += "-06" if (d < 22) else "-07" 
            startdate += "-22" if (d < 22) else "-23" 
            enddate += str(y) 
            enddate += "-07" if (d < 22) else "-08" 
            enddate += "-22" if (d < 22) else "-22"            
        elif(m == 7):
            startdate += str(y) 
            startdate += "-07" if (d < 23) else "-08" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-08" if (d < 23) else "-09" 
            enddate += "-22" if (d < 23) else "-22"            
        elif(m == 8):
            startdate += str(y) 
            startdate += "-08" if (d < 23) else "-09" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-09" if (d < 23) else "-10" 
            enddate += "-22" if (d < 23) else "-22"
        elif(m == 9):
            startdate = str(y) 
            startdate += "-09" if (d < 23) else "-10" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-10" if (d < 23) else "-11" 
            enddate += "-22" if (d < 23) else "-21"            
        elif(m == 10):
            startdate += str(y) 
            startdate += "-10" if (d < 23) else "-11" 
            startdate += "-23" if (d < 23) else "-22" 
            enddate += str(y) 
            enddate += "-11" if (d < 23) else "-12" 
            enddate += "-21" if (d < 23) else "-21"            
        elif(m == 11):
            startdate += str(y) 
            startdate += "-11" if (d < 22) else "-12" 
            startdate += "-22" if (d < 22) else "-22" 
            enddate += str(y) 
            enddate += "-12" if (d < 22) else "-01" 
            enddate += "-21" if (d < 22) else "-20"
        elif(m == 12):
            startdate += str(y) 
            startdate += "-12" if (d < 22) else "-01" 
            startdate += "-22" if (d < 22) else "-21"
            enddate += str(y) 
            enddate += "-01" if (d < 22) else "-02" 
            enddate += "-20" if (d < 22) else "-19"             


        results = Resturaunt_Day_Meal.objects.filter(date__gte=startdate, date__lte=enddate).values('id')

        objs = []
        for dm in results:
            obj = Resturaunt_Day_Meal.objects.get(id=dm['id'])
            obj.isActive = False
            objs.append(obj)
        Resturaunt_Day_Meal.objects.bulk_update(objs, ['isActive'])     

        return Response(
            Resturaunt_Day_Meal.objects.filter(date__gte=startdate, date__lte=enddate).annotate(
                selectedNo=Count('ResturauntDayMeal_ResturauntEmployeeDayMeal')).values('id', 'date', 'totalNo', 'isActive', 'resturaunt_meal', 'selectedNo')
        )  


class Resturaunt_Employee_Day_MealViewSet(viewsets.ModelViewSet):
    queryset = Resturaunt_Employee_Day_Meal.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Resturaunt_Employee_Day_MealProSerializer
    
class Resturaunt_Employee_Day_Meal_Current_MonthViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Resturaunt_Employee_Day_MealSerializer

    def get_queryset(self):
        currentdate = date.today()
        y = currentdate.year
        m = currentdate.month-1
        d = currentdate.day
        startdate = ""
        enddate = ""
        if(m == 1):
            startdate += str(y) 
            startdate += "-01" if (d < 21) else "-02" 
            startdate += "-21" if (d < 21) else "-20"
            enddate += str(y) 
            enddate += "-02" if (d < 21) else "-03" 
            enddate += "-19" if (d < 21) else "-20"
        elif(m == 2):
            startdate += str(y) 
            startdate += "-02" if (d < 20) else "-03" 
            startdate += "-20" if (d < 20) else "-21"
            enddate += str(y) 
            enddate += "-03" if (d < 20) else "-04" 
            enddate += "-20" if (d < 20) else "-20"
        elif(m == 3):
            startdate += str(y) 
            startdate += "-03" if (d < 21) else "-04" 
            startdate += "-21" if (d < 21) else "-21"
            enddate += str(y) 
            enddate += "-04" if (d < 21) else "-05" 
            enddate += "-21" if (d < 21) else "-21"
        elif(m == 4):
            startdate += str(y) 
            startdate += "-04" if (d < 21) else "-05" 
            startdate += "-21" if (d < 21) else "-22"
            enddate += str(y) 
            enddate += "-05" if (d < 21) else "-06" 
            enddate += "-21" if (d < 21) else "-21"            
        elif(m == 5):
            startdate += str(y) 
            startdate += "-05" if (d < 22) else "-06" 
            startdate += "-22" if (d < 22) else "-22" 
            enddate += str(y) 
            enddate += "-06" if (d < 22) else "-07" 
            enddate += "-21" if (d < 22) else "-22"            
        elif(m == 6):
            startdate += str(y) 
            startdate += "-06" if (d < 22) else "-07" 
            startdate += "-22" if (d < 22) else "-23" 
            enddate += str(y) 
            enddate += "-07" if (d < 22) else "-08" 
            enddate += "-22" if (d < 22) else "-22"            
        elif(m == 7):
            startdate += str(y) 
            startdate += "-07" if (d < 23) else "-08" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-08" if (d < 23) else "-09" 
            enddate += "-22" if (d < 23) else "-22"            
        elif(m == 8):
            startdate += str(y) 
            startdate += "-08" if (d < 23) else "-09" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-09" if (d < 23) else "-10" 
            enddate += "-22" if (d < 23) else "-22"
        elif(m == 9):
            startdate = str(y) 
            startdate += "-09" if (d < 23) else "-10" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-10" if (d < 23) else "-11" 
            enddate += "-22" if (d < 23) else "-21"            
        elif(m == 10):
            startdate += str(y) 
            startdate += "-10" if (d < 23) else "-11" 
            startdate += "-23" if (d < 23) else "-22" 
            enddate += str(y) 
            enddate += "-11" if (d < 23) else "-12" 
            enddate += "-21" if (d < 23) else "-21"            
        elif(m == 11):
            startdate += str(y) 
            startdate += "-11" if (d < 22) else "-12" 
            startdate += "-22" if (d < 22) else "-22" 
            enddate += str(y) 
            enddate += "-12" if (d < 22) else "-01" 
            enddate += "-21" if (d < 22) else "-20"
        elif(m == 12):
            startdate += str(y) 
            startdate += "-12" if (d < 22) else "-01" 
            startdate += "-22" if (d < 22) else "-21"
            enddate += str(y) 
            enddate += "-01" if (d < 22) else "-02" 
            enddate += "-20" if (d < 22) else "-19"             
            
        employee_id = self.kwargs['employee_id']
        return Resturaunt_Employee_Day_Meal.objects.filter(employee=employee_id, 
            resturaunt_day_meal__date__gte=startdate, resturaunt_day_meal__date__lte=enddate)

class Resturaunt_Employee_Day_Meal_Next_MonthViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Resturaunt_Employee_Day_MealSerializer

    def get_queryset(self):
        currentdate = date.today()
        y = currentdate.year
        m = currentdate.month
        d = currentdate.day
        startdate = ""
        enddate = ""
        if(m == 1):
            startdate += str(y) 
            startdate += "-01" if (d < 21) else "-02" 
            startdate += "-21" if (d < 21) else "-20"
            enddate += str(y) 
            enddate += "-02" if (d < 21) else "-03" 
            enddate += "-19" if (d < 21) else "-20"
        elif(m == 2):
            startdate += str(y) 
            startdate += "-02" if (d < 20) else "-03" 
            startdate += "-20" if (d < 20) else "-21"
            enddate += str(y) 
            enddate += "-03" if (d < 20) else "-04" 
            enddate += "-20" if (d < 20) else "-20"
        elif(m == 3):
            startdate += str(y) 
            startdate += "-03" if (d < 21) else "-04" 
            startdate += "-21" if (d < 21) else "-21"
            enddate += str(y) 
            enddate += "-04" if (d < 21) else "-05" 
            enddate += "-21" if (d < 21) else "-21"
        elif(m == 4):
            startdate += str(y) 
            startdate += "-04" if (d < 21) else "-05" 
            startdate += "-21" if (d < 21) else "-22"
            enddate += str(y) 
            enddate += "-05" if (d < 21) else "-06" 
            enddate += "-21" if (d < 21) else "-21"            
        elif(m == 5):
            startdate += str(y) 
            startdate += "-05" if (d < 22) else "-06" 
            startdate += "-22" if (d < 22) else "-22" 
            enddate += str(y) 
            enddate += "-06" if (d < 22) else "-07" 
            enddate += "-21" if (d < 22) else "-22"            
        elif(m == 6):
            startdate += str(y) 
            startdate += "-06" if (d < 22) else "-07" 
            startdate += "-22" if (d < 22) else "-23" 
            enddate += str(y) 
            enddate += "-07" if (d < 22) else "-08" 
            enddate += "-22" if (d < 22) else "-22"            
        elif(m == 7):
            startdate += str(y) 
            startdate += "-07" if (d < 23) else "-08" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-08" if (d < 23) else "-09" 
            enddate += "-22" if (d < 23) else "-22"            
        elif(m == 8):
            startdate += str(y) 
            startdate += "-08" if (d < 23) else "-09" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-09" if (d < 21) else "-10" 
            enddate += "-22" if (d < 21) else "-22"
        elif(m == 9):
            startdate = str(y) 
            startdate += "-09" if (d < 23) else "-10" 
            startdate += "-23" if (d < 23) else "-23" 
            enddate += str(y) 
            enddate += "-10" if (d < 21) else "-11" 
            enddate += "-22" if (d < 21) else "-21"            
        elif(m == 10):
            startdate += str(y) 
            startdate += "-10" if (d < 23) else "-11" 
            startdate += "-23" if (d < 23) else "-22" 
            enddate += str(y) 
            enddate += "-11" if (d < 21) else "-12" 
            enddate += "-21" if (d < 21) else "-21"            
        elif(m == 11):
            startdate += str(y) 
            startdate += "-11" if (d < 22) else "-12" 
            startdate += "-22" if (d < 22) else "-22" 
            enddate += str(y) 
            enddate += "-12" if (d < 21) else "-01" 
            enddate += "-21" if (d < 21) else "-20"
        elif(m == 12):
            startdate += str(y) 
            startdate += "-12" if (d < 22) else "-01" 
            startdate += "-22" if (d < 22) else "-21"
            enddate += str(y) 
            enddate += "-01" if (d < 21) else "-02" 
            enddate += "-20" if (d < 21) else "-19"             
            
        employee_id = self.kwargs['employee_id']
        return Resturaunt_Employee_Day_Meal.objects.filter(employee=employee_id, 
            resturaunt_day_meal__date__gte=startdate, resturaunt_day_meal__date__lte=enddate)

class Resturaunt_Employee_Day_MealProViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 
    serializer_class = Resturaunt_Employee_Day_MealExSerializer

    def get(self, request, *args, **kwargs):
        return Response(
            Resturaunt_Employee_Day_Meal.objects.select_related('resturaunt_day_meal').values(
                'id', 'employee', 'resturaunt_day_meal', 'resturaunt_day_meal__resturaunt_meal', 'resturaunt_day_meal__date')
        )

class Resturaunt_Employee_OneDay_MealViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Resturaunt_Employee_Day_MealExSerializer

    def get_queryset(self):
        currentdate = date.today()
        return Resturaunt_Employee_Day_Meal.objects.filter(resturaunt_day_meal__date__exact=currentdate)

class Resturaunt_Save_Current_Month_Employee_Meal_Day(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def post(self, request, *args, **kwargs):
        try:
            import json
            data = request.data
            personelMealDays = data["personelMealDays"]
            editMood = data["editMood"]

            employee_id = personelMealDays[0]['employee']

            currentdate = datetime.today()
            y = currentdate.year
            m = currentdate.month-1
            d = currentdate.day
            startdate = ""
            enddate = ""
            if(m == 1):
                startdate += str(y) 
                startdate += "-01" if (d < 21) else "-02" 
                startdate += "-21" if (d < 21) else "-20"
                enddate += str(y) 
                enddate += "-02" if (d < 21) else "-03" 
                enddate += "-19" if (d < 21) else "-20"
            elif(m == 2):
                startdate += str(y) 
                startdate += "-02" if (d < 20) else "-03" 
                startdate += "-20" if (d < 20) else "-21"
                enddate += str(y) 
                enddate += "-03" if (d < 20) else "-04" 
                enddate += "-20" if (d < 20) else "-20"
            elif(m == 3):
                startdate += str(y) 
                startdate += "-03" if (d < 21) else "-04" 
                startdate += "-21" if (d < 21) else "-21"
                enddate += str(y) 
                enddate += "-04" if (d < 21) else "-05" 
                enddate += "-21" if (d < 21) else "-21"
            elif(m == 4):
                startdate += str(y) 
                startdate += "-04" if (d < 21) else "-05" 
                startdate += "-21" if (d < 21) else "-22"
                enddate += str(y) 
                enddate += "-05" if (d < 21) else "-06" 
                enddate += "-21" if (d < 21) else "-21"            
            elif(m == 5):
                startdate += str(y) 
                startdate += "-05" if (d < 22) else "-06" 
                startdate += "-22" if (d < 22) else "-22" 
                enddate += str(y) 
                enddate += "-06" if (d < 22) else "-07" 
                enddate += "-21" if (d < 22) else "-22"            
            elif(m == 6):
                startdate += str(y) 
                startdate += "-06" if (d < 22) else "-07" 
                startdate += "-22" if (d < 22) else "-23" 
                enddate += str(y) 
                enddate += "-07" if (d < 22) else "-08" 
                enddate += "-22" if (d < 22) else "-22"            
            elif(m == 7):
                startdate += str(y) 
                startdate += "-07" if (d < 23) else "-08" 
                startdate += "-23" if (d < 23) else "-23" 
                enddate += str(y) 
                enddate += "-08" if (d < 23) else "-09" 
                enddate += "-22" if (d < 23) else "-22"            
            elif(m == 8):
                startdate += str(y) 
                startdate += "-08" if (d < 23) else "-09" 
                startdate += "-23" if (d < 23) else "-23" 
                enddate += str(y) 
                enddate += "-09" if (d < 23) else "-10" 
                enddate += "-22" if (d < 23) else "-22"
            elif(m == 9):
                startdate = str(y) 
                startdate += "-09" if (d < 23) else "-10" 
                startdate += "-23" if (d < 23) else "-23" 
                enddate += str(y) 
                enddate += "-10" if (d < 23) else "-11" 
                enddate += "-22" if (d < 23) else "-21"            
            elif(m == 10):
                startdate += str(y) 
                startdate += "-10" if (d < 23) else "-11" 
                startdate += "-23" if (d < 23) else "-22" 
                enddate += str(y) 
                enddate += "-11" if (d < 23) else "-12" 
                enddate += "-21" if (d < 23) else "-21"            
            elif(m == 11):
                startdate += str(y) 
                startdate += "-11" if (d < 22) else "-12" 
                startdate += "-22" if (d < 22) else "-22" 
                enddate += str(y) 
                enddate += "-12" if (d < 22) else "-01" 
                enddate += "-21" if (d < 22) else "-20"
            elif(m == 12):
                startdate += str(y) 
                startdate += "-12" if (d < 22) else "-01" 
                startdate += "-22" if (d < 22) else "-21"
                enddate += str(y) 
                enddate += "-01" if (d < 22) else "-02" 
                enddate += "-20" if (d < 22) else "-19"             

            if(editMood):
                dt = currentdate + timedelta(days=3)
                next3DaysDate = dt.date()

                result = Resturaunt_Employee_Day_Meal.objects.filter(
                    employee=employee_id, 
                    resturaunt_day_meal__date__gte=startdate, 
                    resturaunt_day_meal__date__lte=enddate)

                mealDays = Resturaunt_Day_Meal.objects.filter(date__gte=startdate, date__lte=enddate).filter(date__gt=next3DaysDate)
                mealDayNo = mealDays.count()
                firstMealDay = mealDays.first()
                mealsDayNo =  Resturaunt_Day_Meal.objects.filter(date__exact=firstMealDay.date).count()
                mealSelectedNo = (mealDayNo // mealsDayNo)
                
                if(len(result) == 0 and len(personelMealDays) == mealSelectedNo):
                    objs = []
                    for pmd in personelMealDays:
                        obj = Resturaunt_Employee_Day_Meal(employee_id=pmd['employee'], resturaunt_day_meal_id=pmd['resturaunt_day_meal'])
                        objs.append(obj)
                    Resturaunt_Employee_Day_Meal.objects.bulk_create(objs)   

                return Response(Resturaunt_Employee_Day_Meal.objects.filter(employee=employee_id, 
                    resturaunt_day_meal__date__gte=startdate, resturaunt_day_meal__date__lte=enddate).values('id', 'employee', 'resturaunt_day_meal'))

            else:
                objs = []
                for pmd in personelMealDays:
                    obj = Resturaunt_Employee_Day_Meal.objects.get(id=pmd['id'])
                    obj.resturaunt_day_meal_id = pmd['resturaunt_day_meal']
                    objs.append(obj)
                Resturaunt_Employee_Day_Meal.objects.bulk_update(objs, ['resturaunt_day_meal'])     

                return Response(Resturaunt_Employee_Day_Meal.objects.filter(employee=employee_id, 
                    resturaunt_day_meal__date__gte=startdate, resturaunt_day_meal__date__lte=enddate).values('id', 'employee', 'resturaunt_day_meal'))                         

        except Exception as e:
            return Response(e)     

class Resturaunt_Save_Next_Month_Employee_Meal_Day(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def post(self, request, *args, **kwargs):
        try:
            import json
            data = request.data
            personelMealDays = data["personelMealDays"]
            editMood = data["editMood"]

            employee_id = personelMealDays[0]['employee']

            currentdate = datetime.today()
            y = currentdate.year
            m = currentdate.month
            d = currentdate.day
            startdate = ""
            enddate = ""
            if(m == 1):
                startdate += str(y) 
                startdate += "-01" if (d < 21) else "-02" 
                startdate += "-21" if (d < 21) else "-20"
                enddate += str(y) 
                enddate += "-02" if (d < 21) else "-03" 
                enddate += "-19" if (d < 21) else "-20"
            elif(m == 2):
                startdate += str(y) 
                startdate += "-02" if (d < 20) else "-03" 
                startdate += "-20" if (d < 20) else "-21"
                enddate += str(y) 
                enddate += "-03" if (d < 20) else "-04" 
                enddate += "-20" if (d < 20) else "-20"
            elif(m == 3):
                startdate += str(y) 
                startdate += "-03" if (d < 21) else "-04" 
                startdate += "-21" if (d < 21) else "-21"
                enddate += str(y) 
                enddate += "-04" if (d < 21) else "-05" 
                enddate += "-21" if (d < 21) else "-21"
            elif(m == 4):
                startdate += str(y) 
                startdate += "-04" if (d < 21) else "-05" 
                startdate += "-21" if (d < 21) else "-22"
                enddate += str(y) 
                enddate += "-05" if (d < 21) else "-06" 
                enddate += "-21" if (d < 21) else "-21"            
            elif(m == 5):
                startdate += str(y) 
                startdate += "-05" if (d < 22) else "-06" 
                startdate += "-22" if (d < 22) else "-22" 
                enddate += str(y) 
                enddate += "-06" if (d < 22) else "-07" 
                enddate += "-21" if (d < 22) else "-22"            
            elif(m == 6):
                startdate += str(y) 
                startdate += "-06" if (d < 22) else "-07" 
                startdate += "-22" if (d < 22) else "-23" 
                enddate += str(y) 
                enddate += "-07" if (d < 22) else "-08" 
                enddate += "-22" if (d < 22) else "-22"            
            elif(m == 7):
                startdate += str(y) 
                startdate += "-07" if (d < 23) else "-08" 
                startdate += "-23" if (d < 23) else "-23" 
                enddate += str(y) 
                enddate += "-08" if (d < 23) else "-09" 
                enddate += "-22" if (d < 23) else "-22"            
            elif(m == 8):
                startdate += str(y) 
                startdate += "-08" if (d < 23) else "-09" 
                startdate += "-23" if (d < 23) else "-23" 
                enddate += str(y) 
                enddate += "-09" if (d < 23) else "-10" 
                enddate += "-22" if (d < 23) else "-22"
            elif(m == 9):
                startdate = str(y) 
                startdate += "-09" if (d < 23) else "-10" 
                startdate += "-23" if (d < 23) else "-23" 
                enddate += str(y) 
                enddate += "-10" if (d < 23) else "-11" 
                enddate += "-22" if (d < 23) else "-21"            
            elif(m == 10):
                startdate += str(y) 
                startdate += "-10" if (d < 23) else "-11" 
                startdate += "-23" if (d < 23) else "-22" 
                enddate += str(y) 
                enddate += "-11" if (d < 23) else "-12" 
                enddate += "-21" if (d < 23) else "-21"            
            elif(m == 11):
                startdate += str(y) 
                startdate += "-11" if (d < 22) else "-12" 
                startdate += "-22" if (d < 22) else "-22" 
                enddate += str(y) 
                enddate += "-12" if (d < 22) else "-01" 
                enddate += "-21" if (d < 22) else "-20"
            elif(m == 12):
                startdate += str(y) 
                startdate += "-12" if (d < 22) else "-01" 
                startdate += "-22" if (d < 22) else "-21"
                enddate += str(y) 
                enddate += "-01" if (d < 22) else "-02" 
                enddate += "-20" if (d < 22) else "-19"             

            if(editMood):
                dt = currentdate + timedelta(days=3)
                next3DaysDate = dt.date()

                result = Resturaunt_Employee_Day_Meal.objects.filter(
                    employee=employee_id, 
                    resturaunt_day_meal__date__gte=startdate, 
                    resturaunt_day_meal__date__lte=enddate)

                mealDays = Resturaunt_Day_Meal.objects.filter(date__gte=startdate, date__lte=enddate).filter(date__gt=next3DaysDate)
                mealDayNo = mealDays.count()
                firstMealDay = mealDays.first()
                mealsDayNo =  Resturaunt_Day_Meal.objects.filter(date__exact=firstMealDay.date).count()
                mealSelectedNo = (mealDayNo // mealsDayNo)
                
                if(len(result) == 0 and len(personelMealDays) == mealSelectedNo):
                    objs = []
                    for pmd in personelMealDays:
                        obj = Resturaunt_Employee_Day_Meal(employee_id=pmd['employee'], resturaunt_day_meal_id=pmd['resturaunt_day_meal'])
                        objs.append(obj)
                    Resturaunt_Employee_Day_Meal.objects.bulk_create(objs)   

                return Response(Resturaunt_Employee_Day_Meal.objects.filter(employee=employee_id, 
                    resturaunt_day_meal__date__gte=startdate, resturaunt_day_meal__date__lte=enddate).values('id', 'employee', 'resturaunt_day_meal'))

            else:
                objs = []
                for pmd in personelMealDays:
                    obj = Resturaunt_Employee_Day_Meal.objects.get(id=pmd['id'])
                    obj.resturaunt_day_meal_id = pmd['resturaunt_day_meal']
                    objs.append(obj)
                Resturaunt_Employee_Day_Meal.objects.bulk_update(objs, ['resturaunt_day_meal'])     

                return Response(Resturaunt_Employee_Day_Meal.objects.filter(employee=employee_id, 
                    resturaunt_day_meal__date__gte=startdate, resturaunt_day_meal__date__lte=enddate).values('id', 'employee', 'resturaunt_day_meal'))                         

        except Exception as e:
            return Response(e)
# {'startdate': d1, 'enddate': d2, 'editMood': e, 'X': x, 'Y': y1, 'Z': z, 'Objs': objs, 'M': m}                 

class Resturaunt_Fish_MealViewSet(generics.GenericAPIView):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ] 

    def get(self, request, *args, **kwargs):
        p_code = self.kwargs['code']
        currentdate = date.today()
        emps = Employee.objects.filter(personel_code__exact=p_code)
        if(emps.exists() and len(emps) == 1):
            empid = emps[0].id
            redms = Resturaunt_Employee_Day_Meal.objects.filter(employee__exact=empid, resturaunt_day_meal__date__exact=currentdate, served__exact=False)
            if(redms.exists() and len(redms) == 1):
                rdm_id = redms[0].resturaunt_day_meal.id

                aggregate = Resturaunt_Day_Meal.objects.filter(date=currentdate, id__lte=rdm_id).aggregate(meal_no=Count('id'))
                mealNo = aggregate['meal_no']     

                return Response(
                    Resturaunt_Employee_Day_Meal.objects.filter(employee__exact=empid, resturaunt_day_meal__date__exact=currentdate, served__exact=False
                    ).annotate(meal_no=Value(mealNo, output_field=CharField())).values('id', 'meal_no', 'resturaunt_day_meal__resturaunt_meal__name', 
                            'employee__first_name', 'employee__last_name', 'employee__department__company__name')
                )
        # p_code = self.kwargs['code']
        # currentdate = date.today()
        # emps = Employee.objects.filter(personel_code__exact=p_code)
        # if(emps.exists() and len(emps) == 1):
        #     empid = emps[0].id
        #     redms = Resturaunt_Employee_Day_Meal.objects.filter(employee__exact=empid, resturaunt_day_meal__date__exact=currentdate, served__exact=False)
        #     if(redms.exists() and len(redms) == 1):
        #         return Response(
        #             Resturaunt_Employee_Day_Meal.objects.filter(employee__exact=empid, resturaunt_day_meal__date__exact=currentdate, served__exact=False).values(
        #                 'id', 'resturaunt_day_meal__resturaunt_meal__name', 'employee__first_name', 'employee__last_name', 'employee__department__company__name')
        #         )
        return Response(
            None
        )

class Resturaunt_Served_MealViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated] 

    serializer_class = Resturaunt_Served_MealSerializer

    def get_queryset(self):
        currentdate = date.today()
        return Resturaunt_Day_Meal.objects.filter(date__exact=currentdate).annotate(
            selectedNo=Count('ResturauntDayMeal_ResturauntEmployeeDayMeal')).annotate(
                servedNo=Count('ResturauntDayMeal_ResturauntEmployeeDayMeal', filter=Q(ResturauntDayMeal_ResturauntEmployeeDayMeal__served=True))).annotate(
                    meal_no=Window(
                    expression=RowNumber(),
                    order_by=F('id').asc())
                ).order_by('meal_no', 'id')
        
class Restrant_Set_ServedViewSet(generics.GenericAPIView):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ] 

    def patch(self, request, *args, **kwargs):
        _id = self.kwargs['id']
        redm = Resturaunt_Employee_Day_Meal.objects.get(id=_id)
        redm.served = True
        redm.save()
        return Response(
            'Meal Served'
        )


class Resturaunt_Guest_Day_MealViewSet(viewsets.ModelViewSet):
    queryset = Resturaunt_Guest_Day_Meal.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Resturaunt_Guest_Day_MealSerializer

class Resturaunt_Department_Guest_Day_MealsViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        try:
            selectedDate = self.kwargs['selectedDate']
            departmentId = self.kwargs['departmentId']
            mealDate = datetime.strptime(selectedDate, '%Y-%m-%d').date()

            return Response(
                    Resturaunt_Guest_Day_Meal.objects.filter(
                    ResturauntGuestDayMeal_ResturauntGuestDayMealJunction__resturaunt_day_meal__date__year=mealDate.year, 
                    ResturauntGuestDayMeal_ResturauntGuestDayMealJunction__resturaunt_day_meal__date__month=mealDate.month, 
                    ResturauntGuestDayMeal_ResturauntGuestDayMealJunction__resturaunt_day_meal__date__day=mealDate.day,
                                        department__exact=departmentId).values('id', 'department', 'project', 'description', 
                                        'ResturauntGuestDayMeal_ResturauntGuestDayMealJunction__resturaunt_day_meal__id',
                                        'ResturauntGuestDayMeal_ResturauntGuestDayMealJunction__resturaunt_day_meal__date')
            )
        except Exception as e:
            return Response(e)

class Resturaunt_Project_Guest_Day_MealsViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        try:
            selectedDate = self.kwargs['selectedDate']
            projectId = self.kwargs['projectId']
            mealDate = datetime.strptime(selectedDate, '%Y-%m-%d').date()

            return Response(
                    Resturaunt_Guest_Day_Meal.objects.filter(
                    ResturauntGuestDayMeal_ResturauntGuestDayMealJunction__resturaunt_day_meal__date__year=mealDate.year, 
                    ResturauntGuestDayMeal_ResturauntGuestDayMealJunction__resturaunt_day_meal__date__month=mealDate.month, 
                    ResturauntGuestDayMeal_ResturauntGuestDayMealJunction__resturaunt_day_meal__date__day=mealDate.day,
                                        project__exact=projectId).values('id', 'department', 'project', 'description', 
                                        'ResturauntGuestDayMeal_ResturauntGuestDayMealJunction__resturaunt_day_meal__id',
                                        'ResturauntGuestDayMeal_ResturauntGuestDayMealJunction__resturaunt_day_meal__date')
            )
        except Exception as e:
            return Response(e)

class Resturaunt_Edit_Guest_Day_MealsViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            id = data["id"]
            departmentId = data["departmentId"]
            description = data["description"]

            guest_day_meal = Resturaunt_Guest_Day_Meal.objects.get(pk=id)
            guest_day_meal.department_id = departmentId
            guest_day_meal.description = description
            guest_day_meal.save()

            return Response(
                    Resturaunt_Guest_Day_Meal.objects.filter(id__exact=id).values('id', 'department', 'project', 'description', 
                                        'ResturauntGuestDayMeal_ResturauntGuestDayMealJunction__resturaunt_day_meal__id',
                                        'ResturauntGuestDayMeal_ResturauntGuestDayMealJunction__resturaunt_day_meal__date')
            )
        except Exception as e:
            return Response(e)            

class Resturaunt_Department_Day_MealsAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        try:
            selectedDate = self.kwargs['selectedDate']
            departmentId = self.kwargs['departmentId']
            mealDate = datetime.strptime(selectedDate, '%Y-%m-%d').date()

            results1 = Resturaunt_Day_Meal.objects.filter(date__year=mealDate.year, 
                                                date__month=mealDate.month, 
                                                date__day=mealDate.day).values(
                                                    'id', 'date', 'resturaunt_meal__name', 'totalNo', 
                                                    'ResturauntDayMeal_ResturauntGuestDayMealJunction__id',
                                                    'ResturauntDayMeal_ResturauntGuestDayMealJunction__qty')

            results2 = Resturaunt_Day_Meal.objects.filter(date__year=mealDate.year, 
                                                date__month=mealDate.month, 
                                                date__day=mealDate.day,
                                                resturaunt_guest_day_meal__department__exact=departmentId).values(
                                                    'id', 'date', 'resturaunt_meal__name', 'totalNo', 
                                                    'ResturauntDayMeal_ResturauntGuestDayMealJunction__id',
                                                    'ResturauntDayMeal_ResturauntGuestDayMealJunction__qty')

            if(len(results1) != 0 and len(results2) == 0):
                return Response(results1)
            else:
                return Response(results2)                                        
        except Exception as e:
            return Response(e)

class Resturaunt_Project_Day_MealsAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        try:
            selectedDate = self.kwargs['selectedDate']
            projectId = self.kwargs['projectId']
            mealDate = datetime.strptime(selectedDate, '%Y-%m-%d').date()

            results1 = Resturaunt_Day_Meal.objects.filter(date__year=mealDate.year, 
                                                date__month=mealDate.month, 
                                                date__day=mealDate.day).values(
                                                    'id', 'date', 'resturaunt_meal__name', 'totalNo', 
                                                    'ResturauntDayMeal_ResturauntGuestDayMealJunction__id',
                                                    'ResturauntDayMeal_ResturauntGuestDayMealJunction__qty')

            results2 = Resturaunt_Day_Meal.objects.filter(date__year=mealDate.year, 
                                                date__month=mealDate.month, 
                                                date__day=mealDate.day,
                                                resturaunt_guest_day_meal__project__exact=projectId).values(
                                                    'id', 'date', 'resturaunt_meal__name', 'totalNo', 
                                                    'ResturauntDayMeal_ResturauntGuestDayMealJunction__id',
                                                    'ResturauntDayMeal_ResturauntGuestDayMealJunction__qty')

            if(len(results1) != 0 and len(results2) == 0):
                # department = Department.objects.get(pk=departmentId)
                # guest_day_meal = Resturaunt_Guest_Day_Meal(department=department, description='')
                # guest_day_meal.save()
                return Response(results1)
            else:
                return Response(results2)                                        
        except Exception as e:
            return Response(e)


class Resturaunt_Edit_Guest_Day_MealsJunction(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    
    def post(self, request, *args, **kwargs):
        data = request.data
        departmentId = data["departmentId"]
        id = data["id"]
        mealDayId = data["mealDayId"]
        guestMealDayId = data["guestMealDayId"]
        qty = data["qty"]
        mood = data["mood"]

        day_meal = Resturaunt_Day_Meal.objects.get(pk=mealDayId)
        mealDate = day_meal.date

        if(mood == 1):
            guest_day_meal = Resturaunt_Guest_Day_Meal(department_id=departmentId, description='')
            guest_day_meal.save()
            guestMealDayId = guest_day_meal.id

            guest_day_meal_junction = Resturaunt_Guest_Day_Meal_Junction(resturaunt_day_meal_id=mealDayId, 
                                                                        resturaunt_guest_day_meal_id=guestMealDayId,
                                                                        qty=qty)
            guest_day_meal_junction.save()
        elif(mood == 2):
            guest_day_meal_junction = Resturaunt_Guest_Day_Meal_Junction(resturaunt_day_meal_id=mealDayId, 
                                                                        resturaunt_guest_day_meal_id=guestMealDayId,
                                                                        qty=qty)
            guest_day_meal_junction.save()
        elif(mood == 3):
            guest_day_meal_junction = Resturaunt_Guest_Day_Meal_Junction.objects.get(resturaunt_day_meal_id=mealDayId, 
                                                                        resturaunt_guest_day_meal_id=guestMealDayId)
            guest_day_meal_junction.qty = qty
            guest_day_meal_junction.save()

        results1 = Resturaunt_Day_Meal.objects.filter(date__exact=mealDate,
                                                resturaunt_guest_day_meal__id__exact=guestMealDayId)
        results2 = Resturaunt_Day_Meal.objects.filter(date__exact=mealDate,
                                                resturaunt_guest_day_meal__id__exact=guestMealDayId).values(
                                                'id', 'date', 'resturaunt_meal__name', 'totalNo', 
                                                'ResturauntDayMeal_ResturauntGuestDayMealJunction__id',
                                                'ResturauntDayMeal_ResturauntGuestDayMealJunction__qty')


        results3 = Resturaunt_Day_Meal.objects.filter(date__exact=mealDate).exclude(id__in=results1).values(
                                                'id', 'date', 'resturaunt_meal__name', 'totalNo', 
                                                'ResturauntDayMeal_ResturauntGuestDayMealJunction__id',
                                                'ResturauntDayMeal_ResturauntGuestDayMealJunction__qty')
        reuslts3 = results3.union(results2)

        return Response(reuslts3) 

class Resturaunt_DepartmentsMealsDailyListViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        try:
            currentdate = date.today()
            departmentId = self.kwargs['departmentId']
            # date = datetime.strptime(currentdate, '%Y-%m-%d').date()

            result1 = Resturaunt_Day_Meal.objects.filter(date__exact=currentdate)
            result = Resturaunt_Employee_Day_Meal.objects.filter(resturaunt_day_meal__in=result1, employee__department_id__exact=departmentId).values(
                                'employee__first_name', 'employee__last_name', 'resturaunt_day_meal__resturaunt_meal__name').order_by(
                                'resturaunt_day_meal__resturaunt_meal__name')
            return Response(result)                   
        except Exception as e:
            return Response(e)        

class Resturaunt_ProjectsMealsDailyListViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        try:
            currentdate = date.today()
            projectId = self.kwargs['projectId']
            # date = datetime.strptime(currentdate, '%Y-%m-%d').date()

            result1 = Resturaunt_Day_Meal.objects.filter(date__exact=currentdate)
            result = Resturaunt_Employee_Day_Meal.objects.filter(resturaunt_day_meal__in=result1, employee__project_id__exact=projectId).values(
                                'employee__first_name', 'employee__last_name', 'resturaunt_day_meal__resturaunt_meal__name').order_by(
                                'resturaunt_day_meal__resturaunt_meal__name')
            return Response(result)                   
        except Exception as e:
            return Response(e)  

class Resturaunt_SectionsMealsDailyListViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        try:
            currentdate = date.today()
            employeeId = self.kwargs['employeeId']

            departmentId = Employee.objects.get(pk=employeeId).department_id
            projectId = Employee.objects.get(pk=employeeId).project_id

            if(projectId == None):
                result1 = Resturaunt_Day_Meal.objects.filter(date__exact=currentdate)
                result = Resturaunt_Employee_Day_Meal.objects.filter(resturaunt_day_meal__in=result1, employee__department_id__exact=departmentId).values(
                                'employee__first_name', 'employee__last_name', 'resturaunt_day_meal__resturaunt_meal__name').order_by(
                                'resturaunt_day_meal__resturaunt_meal__name')
            elif(departmentId == None):
                result1 = Resturaunt_Day_Meal.objects.filter(date__exact=currentdate)
                result = Resturaunt_Employee_Day_Meal.objects.filter(resturaunt_day_meal__in=result1, employee__project_id__exact=projectId).values(
                                'employee__first_name', 'employee__last_name', 'resturaunt_day_meal__resturaunt_meal__name').order_by(
                                'resturaunt_day_meal__resturaunt_meal__name')

            return Response(result)                   
        except Exception as e:
            return Response(e)   

class Resturaunt_Section_NameViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        try:
            employeeId = self.kwargs['employeeId']

            departmentId = Employee.objects.get(pk=employeeId).department_id
            projectId = Employee.objects.get(pk=employeeId).project_id

            if(projectId == None):
                section_name = Department.objects.get(pk=departmentId).name
            elif(departmentId == None):
                section_name = Project.objects.get(pk=projectId).name

            return Response(section_name)                   
        except Exception as e:
            return Response(e)   

class Resturaunt_Save_Guest_Day_MealsJunction(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    
    def post(self, request, *args, **kwargs):
        data = request.data
        departmentId = data["departmentId"]
        projectId = data["projectId"]
        description = data["description"]
        mealDayId = data["mealDayId"]
        mealsNo = data["mealsNo"]

        day_meal = Resturaunt_Day_Meal.objects.get(pk=mealDayId)
        mealDate = day_meal.date

        if(mood == 1):
            guest_day_meal = Resturaunt_Guest_Day_Meal(department_id=departmentId, description=description)
            guest_day_meal.save()
            guestMealDayId = guest_day_meal.id

            guest_day_meal_junction = Resturaunt_Guest_Day_Meal_Junction(resturaunt_day_meal_id=mealDayId, 
                                                                        resturaunt_guest_day_meal_id=guestMealDayId,
                                                                        qty=qty)
            guest_day_meal_junction.save()
        elif(mood == 2):
            guest_day_meal_junction = Resturaunt_Guest_Day_Meal_Junction(resturaunt_day_meal_id=mealDayId, 
                                                                        resturaunt_guest_day_meal_id=guestMealDayId,
                                                                        qty=qty)
            guest_day_meal_junction.save()
        elif(mood == 3):
            guest_day_meal_junction = Resturaunt_Guest_Day_Meal_Junction.objects.get(resturaunt_day_meal_id=mealDayId, 
                                                                        resturaunt_guest_day_meal_id=guestMealDayId)
            guest_day_meal_junction.qty = qty
            guest_day_meal_junction.save()

        results1 = Resturaunt_Day_Meal.objects.filter(date__exact=mealDate,
                                                resturaunt_guest_day_meal__id__exact=guestMealDayId)
        results2 = Resturaunt_Day_Meal.objects.filter(date__exact=mealDate,
                                                resturaunt_guest_day_meal__id__exact=guestMealDayId).values(
                                                'id', 'date', 'resturaunt_meal__name', 'totalNo', 
                                                'ResturauntDayMeal_ResturauntGuestDayMealJunction__id',
                                                'ResturauntDayMeal_ResturauntGuestDayMealJunction__qty')


        results3 = Resturaunt_Day_Meal.objects.filter(date__exact=mealDate).exclude(id__in=results1).values(
                                                'id', 'date', 'resturaunt_meal__name', 'totalNo', 
                                                'ResturauntDayMeal_ResturauntGuestDayMealJunction__id',
                                                'ResturauntDayMeal_ResturauntGuestDayMealJunction__qty')
        reuslts3 = results3.union(results2)

        return Response(reuslts3) 

class Resturaunt_CurrentMonthSelectedMealsViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    # serializer_class = Resturaunt_Employee_Day_MealExSerializer

    def get(self, request, *args, **kwargs):
    # def get_queryset(self):
        currentdate = date.today()
        y = currentdate.year
        m = currentdate.month
        d = currentdate.day
        startdate = ""
        enddate = ""
        if(m == 1):
            startdate += str(y-1) if (d < 21) else str(y)  
            startdate += "-12" if (d < 21) else "-01" 
            startdate += "-22" if (d < 21) else "-21"
            
            enddate += str(y)  
            enddate += "-01" if (d < 21) else "-02" 
            enddate += "-20" if (d < 21) else "-19"
        elif(m == 2):
            startdate += str(y) 
            startdate += "-01" if (d < 20) else "-02" 
            startdate += "-21" if (d < 20) else "-20"
                
            enddate += str(y)  
            enddate += "-02" if (d < 20) else "-03" 
            enddate += "-19" if (d < 20) else "-20"
        elif(m == 3):
            startdate += str(y) 
            startdate += "-02" if (d < 21) else "-03" 
            startdate += "-20" if (d < 21) else "-21"
                
            enddate += str(y)  
            enddate += "-03" if (d < 21) else "-04" 
            enddate += "-20" if (d < 21) else "-20"
        elif(m == 4):
            startdate += str(y) 
            startdate += "-03" if (d < 21) else "-04" 
            startdate += "-21" if (d < 21) else "-21"
                
            enddate += str(y)  
            enddate += "-04" if (d < 21) else "-05" 
            enddate += "-20" if (d < 21) else "-21"
        elif(m == 5):
            startdate += str(y) 
            startdate += "-04" if (d < 22) else "-05" 
            startdate += "-21" if (d < 22) else "-22" 
                
            enddate += str(y)  
            enddate += "-05" if (d < 22) else "-06" 
            enddate += "-21" if (d < 22) else "-21"
        elif(m == 6):
            startdate += str(y) 
            startdate += "-05" if (d < 22) else "-06" 
            startdate += "-22" if (d < 22) else "-22" 
                
            enddate += str(y)  
            enddate += "-06" if (d < 22) else "-06" 
            enddate += "-21" if (d < 22) else "-22"
        elif(m == 7):
            startdate += str(y) 
            startdate += "-06" if (d < 23) else "-07" 
            startdate += "-23" if (d < 23) else "-23" 
                
            enddate += str(y)  
            enddate += "-07" if (d < 23) else "-08" 
            enddate += "-22" if (d < 23) else "-22"
        elif(m == 8):
            startdate += str(y) 
            startdate += "-07" if (d < 23) else "-08" 
            startdate += "-23" if (d < 23) else "-23" 
                
            enddate += str(y)  
            enddate += "-08" if (d < 23) else "-09" 
            enddate += "-22" if (d < 23) else "-22"
        elif(m == 9):
            startdate = str(y) 
            startdate += "-08" if (d < 23) else "-09" 
            startdate += "-23" if (d < 23) else "-23" 
                
            enddate += str(y)  
            enddate += "-09" if (d < 23) else "-10" 
            enddate += "-22" if (d < 23) else "-22"
        elif(m == 10):
            startdate += str(y) 
            startdate += "-09" if (d < 23) else "-10" 
            startdate += "-23" if (d < 23) else "-23" 
                
            enddate += str(y)  
            enddate += "-10" if (d < 23) else "-11" 
            enddate += "-22" if (d < 23) else "-21"
        elif(m == 11):
            startdate += str(y) 
            startdate += "-10" if (d < 22) else "-11" 
            startdate += "-23" if (d < 22) else "-22" 
                
            enddate += str(y)  
            enddate += "-11" if (d < 22) else "-12" 
            enddate += "-21" if (d < 22) else "-21"
        elif(m == 12):
            startdate += str(y) 
            startdate += "-11" if (d < 22) else "-12" 
            startdate += "-22" if (d < 22) else "-22" 
                
            enddate += str(y) if (d < 22) else str(y+1)
            enddate += "-12" if (d < 22) else "-01" 
            enddate += "-21" if (d < 22) else "-20"
            
        employee_id = self.kwargs['employeeId']
        # , resturaunt_day_meal__date__lte=enddate
        return Response(Resturaunt_Employee_Day_Meal.objects.filter( 
            employee=employee_id, resturaunt_day_meal__date__gte=startdate
            ).order_by('-resturaunt_day_meal__date').values('resturaunt_day_meal__date', 
            'resturaunt_day_meal__resturaunt_meal__name')[::-1])

class Resturaunt_AsftDayMealsStatisticsViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        date = self.kwargs['date']
        results1 = Resturaunt_Employee_Day_Meal.objects.filter(resturaunt_day_meal__date__exact=date, 
                employee__department__company__name__exact='آسفالت طوس').exclude(
                employee__department__exact=None).values('employee__department').annotate(
                section=F('employee__department__name'), 
                meal_name=F('resturaunt_day_meal__resturaunt_meal__name'), 
                meal_no=Count('resturaunt_day_meal__resturaunt_meal__name'),
                section_type=Value(1, output_field=SmallIntegerField())).values('section_type', 'section', 'meal_name', 'meal_no')

        results2 = Resturaunt_Employee_Day_Meal.objects.filter(resturaunt_day_meal__date__exact=date).exclude(
                employee__project__exact=None).values('employee__project').annotate(
                section=F('employee__project__name'), 
                meal_name=F('resturaunt_day_meal__resturaunt_meal__name'), 
                meal_no=Count('resturaunt_day_meal__resturaunt_meal__name'),
                section_type=Value(2, output_field=SmallIntegerField())).values('section_type', 'section', 'meal_name', 'meal_no')

        results = results1.union(results2).order_by('section_type', 'section', 'meal_name')
        return Response(results)

class Resturaunt_CompanysDayMealsStatisticsViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        # currentdate = date.today()
        date = self.kwargs['date']
        results = Resturaunt_Employee_Day_Meal.objects.filter(resturaunt_day_meal__date__exact=date).exclude(
        employee__department__company__name__exact='آسفالت طوس').exclude(employee__department__exact=None).values(
            'employee__department').order_by('employee__department__name').annotate(
        section=F('employee__department__name'), 
        meal_name=F('resturaunt_day_meal__resturaunt_meal__name'), 
        meal_no=Count('resturaunt_day_meal__resturaunt_meal__name')).values('section', 'meal_name', 'meal_no')
        return Response(results)        

class Resturaunt_SectionDayMealsStatisticsViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        employeeId = self.kwargs['employeeId']
        currentdate = date.today()

        emp = Employee.objects.get(pk=employeeId)
        department_id = emp.department
        project_id = emp.project

        results = Resturaunt_Employee_Day_Meal.objects.filter(resturaunt_day_meal__date__exact=currentdate,  
            employee__department__exact=department_id, employee__project__exact=project_id).values(
            'employee__department').order_by('employee__department__name').annotate(
            section=F('employee__department__name'), 
            meal_name=F('resturaunt_day_meal__resturaunt_meal__name'), 
            meal_no=Count('resturaunt_day_meal__resturaunt_meal__name')).values(
            'section', 'meal_name', 'meal_no')

        return Response(results)       

class Resturaunt_DepartmentDayMealsStatisticsViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        department_id = self.kwargs['departmentId']
        currentdate = date.today()

        results = Resturaunt_Employee_Day_Meal.objects.filter(
            resturaunt_day_meal__date__exact=currentdate,  
            employee__department__exact=department_id).values(
            'employee__department').order_by('employee__department__name').annotate(
            section=F('employee__department__name'), 
            meal_name=F('resturaunt_day_meal__resturaunt_meal__name'), 
            meal_no=Count('resturaunt_day_meal__resturaunt_meal__name')).values(
            'section', 'meal_name', 'meal_no')

        return Response(results)  

class Resturaunt_ProjectDayMealsStatisticsViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        project_id = self.kwargs['projectId']
        currentdate = date.today()

        results = Resturaunt_Employee_Day_Meal.objects.filter(
            resturaunt_day_meal__date__exact=currentdate,  
            employee__project__exact=project_id).values(
            'employee__project').order_by('employee__project__name').annotate(
            section=F('employee__project__name'), 
            meal_name=F('resturaunt_day_meal__resturaunt_meal__name'), 
            meal_no=Count('resturaunt_day_meal__resturaunt_meal__name')).values(
            'section', 'meal_name', 'meal_no')

        return Response(results)                  

class Resturaunt_ContractorMonthlyMealsStatisticsViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        # def get_queryset(self):
        currentdate = date.today()
        y = currentdate.year
        m = currentdate.month
        d = currentdate.day
        startdate = ""
        enddate = ""
        if(m == 1):
            startdate += str(y-1) if (d < 21) else str(y)  
            startdate += "-12" if (d < 21) else "-01" 
            startdate += "-22" if (d < 21) else "-21"
            
            enddate += str(y)  
            enddate += "-01" if (d < 21) else "-02" 
            enddate += "-20" if (d < 21) else "-19"
        elif(m == 2):
            startdate += str(y) 
            startdate += "-01" if (d < 20) else "-02" 
            startdate += "-21" if (d < 20) else "-20"
                
            enddate += str(y)  
            enddate += "-02" if (d < 20) else "-03" 
            enddate += "-19" if (d < 20) else "-20"
        elif(m == 3):
            startdate += str(y) 
            startdate += "-02" if (d < 21) else "-03" 
            startdate += "-20" if (d < 21) else "-21"
                
            enddate += str(y)  
            enddate += "-03" if (d < 21) else "-04" 
            enddate += "-20" if (d < 21) else "-20"
        elif(m == 4):
            startdate += str(y) 
            startdate += "-03" if (d < 21) else "-04" 
            startdate += "-21" if (d < 21) else "-21"
                
            enddate += str(y)  
            enddate += "-04" if (d < 21) else "-05" 
            enddate += "-20" if (d < 21) else "-21"
        elif(m == 5):
            startdate += str(y) 
            startdate += "-04" if (d < 22) else "-05" 
            startdate += "-21" if (d < 22) else "-22" 
                
            enddate += str(y)  
            enddate += "-05" if (d < 22) else "-06" 
            enddate += "-21" if (d < 22) else "-21"
        elif(m == 6):
            startdate += str(y) 
            startdate += "-05" if (d < 22) else "-06" 
            startdate += "-22" if (d < 22) else "-22" 
                
            enddate += str(y)  
            enddate += "-06" if (d < 22) else "-06" 
            enddate += "-21" if (d < 22) else "-22"
        elif(m == 7):
            startdate += str(y) 
            startdate += "-06" if (d < 23) else "-07" 
            startdate += "-23" if (d < 23) else "-23" 
                
            enddate += str(y)  
            enddate += "-07" if (d < 23) else "-08" 
            enddate += "-22" if (d < 23) else "-22"
        elif(m == 8):
            startdate += str(y) 
            startdate += "-07" if (d < 23) else "-08" 
            startdate += "-23" if (d < 23) else "-23" 
                
            enddate += str(y)  
            enddate += "-08" if (d < 23) else "-09" 
            enddate += "-22" if (d < 23) else "-22"
        elif(m == 9):
            startdate = str(y) 
            startdate += "-08" if (d < 23) else "-09" 
            startdate += "-23" if (d < 23) else "-23" 
                
            enddate += str(y)  
            enddate += "-09" if (d < 23) else "-10" 
            enddate += "-22" if (d < 23) else "-22"
        elif(m == 10):
            startdate += str(y) 
            startdate += "-09" if (d < 23) else "-10" 
            startdate += "-23" if (d < 23) else "-23" 
                
            enddate += str(y)  
            enddate += "-10" if (d < 23) else "-11" 
            enddate += "-22" if (d < 23) else "-21"
        elif(m == 11):
            startdate += str(y) 
            startdate += "-10" if (d < 22) else "-11" 
            startdate += "-23" if (d < 22) else "-22" 
                
            enddate += str(y)  
            enddate += "-11" if (d < 22) else "-12" 
            enddate += "-21" if (d < 22) else "-21"
        elif(m == 12):
            startdate += str(y) 
            startdate += "-11" if (d < 22) else "-12" 
            startdate += "-22" if (d < 22) else "-22" 
                
            enddate += str(y) if (d < 22) else str(y+1)
            enddate += "-12" if (d < 22) else "-01" 
            enddate += "-21" if (d < 22) else "-20"

        results = Resturaunt_Employee_Day_Meal.objects.filter(resturaunt_day_meal__date__gte=startdate).exclude(
            Q(resturaunt_day_meal__resturaunt_meal__name__exact='عدم انتخاب') |
            Q(resturaunt_day_meal__resturaunt_meal__name__exact='عدم حضور')).values(
            'resturaunt_day_meal__resturaunt_meal').order_by('resturaunt_day_meal__date', 'resturaunt_day_meal__resturaunt_meal__name').annotate(
                date=F('resturaunt_day_meal__date'), 
                meal_name=F('resturaunt_day_meal__resturaunt_meal__name'), 
                meal_no=Count('resturaunt_day_meal__resturaunt_meal__name')).values('date', 'meal_name', 'meal_no')
        return Response(results)                   

class Resturaunt_MealsStatisticsDatesListViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        # def get_queryset(self):
        currentdate = date.today()
        y = currentdate.year
        m = currentdate.month
        d = currentdate.day
        startdate = ""
        enddate = ""
        if(m == 1):
            startdate += str(y-1) if (d < 21) else str(y)  
            startdate += "-12" if (d < 21) else "-01" 
            startdate += "-22" if (d < 21) else "-21"
            
            enddate += str(y)  
            enddate += "-01" if (d < 21) else "-02" 
            enddate += "-20" if (d < 21) else "-19"
        elif(m == 2):
            startdate += str(y) 
            startdate += "-01" if (d < 20) else "-02" 
            startdate += "-21" if (d < 20) else "-20"
                
            enddate += str(y)  
            enddate += "-02" if (d < 20) else "-03" 
            enddate += "-19" if (d < 20) else "-20"
        elif(m == 3):
            startdate += str(y) 
            startdate += "-02" if (d < 21) else "-03" 
            startdate += "-20" if (d < 21) else "-21"
                
            enddate += str(y)  
            enddate += "-03" if (d < 21) else "-04" 
            enddate += "-20" if (d < 21) else "-20"
        elif(m == 4):
            startdate += str(y) 
            startdate += "-03" if (d < 21) else "-04" 
            startdate += "-21" if (d < 21) else "-21"
                
            enddate += str(y)  
            enddate += "-04" if (d < 21) else "-05" 
            enddate += "-20" if (d < 21) else "-21"
        elif(m == 5):
            startdate += str(y) 
            startdate += "-04" if (d < 22) else "-05" 
            startdate += "-21" if (d < 22) else "-22" 
                
            enddate += str(y)  
            enddate += "-05" if (d < 22) else "-06" 
            enddate += "-21" if (d < 22) else "-21"
        elif(m == 6):
            startdate += str(y) 
            startdate += "-05" if (d < 22) else "-06" 
            startdate += "-22" if (d < 22) else "-22" 
                
            enddate += str(y)  
            enddate += "-06" if (d < 22) else "-06" 
            enddate += "-21" if (d < 22) else "-22"
        elif(m == 7):
            startdate += str(y) 
            startdate += "-06" if (d < 23) else "-07" 
            startdate += "-23" if (d < 23) else "-23" 
                
            enddate += str(y)  
            enddate += "-07" if (d < 23) else "-08" 
            enddate += "-22" if (d < 23) else "-22"
        elif(m == 8):
            startdate += str(y) 
            startdate += "-07" if (d < 23) else "-08" 
            startdate += "-23" if (d < 23) else "-23" 
                
            enddate += str(y)  
            enddate += "-08" if (d < 23) else "-09" 
            enddate += "-22" if (d < 23) else "-22"
        elif(m == 9):
            startdate = str(y) 
            startdate += "-08" if (d < 23) else "-09" 
            startdate += "-23" if (d < 23) else "-23" 
                
            enddate += str(y)  
            enddate += "-09" if (d < 23) else "-10" 
            enddate += "-22" if (d < 23) else "-22"
        elif(m == 10):
            startdate += str(y) 
            startdate += "-09" if (d < 23) else "-10" 
            startdate += "-23" if (d < 23) else "-23" 
                
            enddate += str(y)  
            enddate += "-10" if (d < 23) else "-11" 
            enddate += "-22" if (d < 23) else "-21"
        elif(m == 11):
            startdate += str(y) 
            startdate += "-10" if (d < 22) else "-11" 
            startdate += "-23" if (d < 22) else "-22" 
                
            enddate += str(y)  
            enddate += "-11" if (d < 22) else "-12" 
            enddate += "-21" if (d < 22) else "-21"
        elif(m == 12):
            startdate += str(y) 
            startdate += "-11" if (d < 22) else "-12" 
            startdate += "-22" if (d < 22) else "-22" 
                
            enddate += str(y) if (d < 22) else str(y+1)
            enddate += "-12" if (d < 22) else "-01" 
            enddate += "-21" if (d < 22) else "-20"

        results = Resturaunt_Employee_Day_Meal.objects.filter(resturaunt_day_meal__date__gte=startdate).values(
            'resturaunt_day_meal__date').annotate(date=F('resturaunt_day_meal__date'),
                date_no=Count('resturaunt_day_meal__date')).values('date').order_by('resturaunt_day_meal__date')

        return Response(results)                   

class Resturaunt_Contractor_Daily_Section_Meals_StatisticsViewAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        # def get_queryset(self):
        currentdate = date.today()    

        result1 = Resturaunt_Employee_Day_Meal.objects.filter(
            resturaunt_day_meal__date__exact=currentdate).exclude(
            employee__department__exact=None).filter( 
            employee__department__company__name__exact='آسفالت طوس').exclude( 
            resturaunt_day_meal__resturaunt_meal__name__in=('عدم حضور', 'عدم انتخاب')).values(
            'employee__department__name',
            'resturaunt_day_meal__resturaunt_meal__name')
        pivot_table1 = pivot(result1, 
                            'employee__department__name', 
                            'resturaunt_day_meal__resturaunt_meal__name', 
                            'employee__department__name', 
                            aggregation=Count)

        result2 = Resturaunt_Employee_Day_Meal.objects.filter(
            resturaunt_day_meal__date__exact=currentdate,
            employee__project__company__name__exact='آسفالت طوس').exclude(    
            employee__project__exact=None).exclude(
            resturaunt_day_meal__resturaunt_meal__name__in=('عدم حضور', 'عدم انتخاب')).values(
            'employee__project__name',
            'resturaunt_day_meal__resturaunt_meal__name')
        pivot_table2 = pivot(result2, 
                            'employee__project__name', 
                            'resturaunt_day_meal__resturaunt_meal__name', 
                            'employee__project__name', 
                            aggregation=Count)

        result3 = Resturaunt_Employee_Day_Meal.objects.filter(
            resturaunt_day_meal__date__exact=currentdate).exclude(
            employee__department__exact=None).exclude(
            employee__department__company__name__exact='آسفالت طوس').exclude(
            resturaunt_day_meal__resturaunt_meal__name__in=('عدم حضور', 'عدم انتخاب')).values(
            'employee__department__name',
            'resturaunt_day_meal__resturaunt_meal__name')
        pivot_table3 = pivot(result3, 
                            'employee__department__name', 
                            'resturaunt_day_meal__resturaunt_meal__name', 
                            'employee__department__name', 
                            aggregation=Count)

        result = pivot_table1.union(pivot_table2).union(pivot_table3)
        return Response(result)
        
class Resturaunt_Day_Meals_NamesViewAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        try:
        # def get_queryset(self):
            currentdate = date.today() 

            result = Resturaunt_Day_Meal.objects.filter(date__exact=currentdate).exclude(
                resturaunt_meal__name__in=('عدم انتخاب', 'عدم حضور')).values('resturaunt_meal__name').order_by('resturaunt_meal__name')   

            return Response(result)
        except Exception as ex:
            return Response('error: ', ex)

class Resturaunt_Day_Meals_TotalNoViewAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        try:
            currentdate = date.today()

            result = Resturaunt_Employee_Day_Meal.objects.filter(
                resturaunt_day_meal__date__exact=currentdate).exclude( 
                resturaunt_day_meal__resturaunt_meal__name__in=('عدم حضور', 'عدم انتخاب')).values(
                'resturaunt_day_meal__resturaunt_meal__name').annotate(
                meal_name=F('resturaunt_day_meal__resturaunt_meal__name'), 
                meal_no=Count('resturaunt_day_meal__resturaunt_meal__name')).values(
                'meal_name', 'meal_no')

            return Response(result)
        except Exception as ex:
            return Response('error: ', ex)   

class Resturaunt_Personel_Didnot_Select_Next_Month_MealsViewAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        try:
            currentdate = date.today()
            y = currentdate.year
            m = currentdate.month
            d = currentdate.day
            startdate = ""
            enddate = ""
            if(m == 1):
                startdate += str(y) 
                startdate += "-01" if (d < 21) else "-02" 
                startdate += "-21" if (d < 21) else "-20"
                enddate += str(y) 
                enddate += "-02" if (d < 21) else "-03" 
                enddate += "-19" if (d < 21) else "-20"
            elif(m == 2):
                startdate += str(y) 
                startdate += "-02" if (d < 20) else "-03" 
                startdate += "-20" if (d < 20) else "-21"
                enddate += str(y) 
                enddate += "-03" if (d < 20) else "-04" 
                enddate += "-20" if (d < 20) else "-20"
            elif(m == 3):
                startdate += str(y) 
                startdate += "-03" if (d < 21) else "-04" 
                startdate += "-21" if (d < 21) else "-21"
                enddate += str(y) 
                enddate += "-04" if (d < 21) else "-05" 
                enddate += "-21" if (d < 21) else "-21"
            elif(m == 4):
                startdate += str(y) 
                startdate += "-04" if (d < 21) else "-05" 
                startdate += "-21" if (d < 21) else "-22"
                enddate += str(y) 
                enddate += "-05" if (d < 21) else "-06" 
                enddate += "-21" if (d < 21) else "-21"            
            elif(m == 5):
                startdate += str(y) 
                startdate += "-05" if (d < 22) else "-06" 
                startdate += "-22" if (d < 22) else "-22" 
                enddate += str(y) 
                enddate += "-06" if (d < 22) else "-07" 
                enddate += "-21" if (d < 22) else "-22"            
            elif(m == 6):
                startdate += str(y) 
                startdate += "-06" if (d < 22) else "-07" 
                startdate += "-22" if (d < 22) else "-23" 
                enddate += str(y) 
                enddate += "-07" if (d < 22) else "-08" 
                enddate += "-22" if (d < 22) else "-22"            
            elif(m == 7):
                startdate += str(y) 
                startdate += "-07" if (d < 23) else "-08" 
                startdate += "-23" if (d < 23) else "-23" 
                enddate += str(y) 
                enddate += "-08" if (d < 23) else "-09" 
                enddate += "-22" if (d < 23) else "-22"            
            elif(m == 8):
                startdate += str(y) 
                startdate += "-08" if (d < 23) else "-09" 
                startdate += "-23" if (d < 23) else "-23" 
                enddate += str(y) 
                enddate += "-09" if (d < 23) else "-10" 
                enddate += "-22" if (d < 23) else "-22"
            elif(m == 9):
                startdate = str(y) 
                startdate += "-09" if (d < 23) else "-10" 
                startdate += "-23" if (d < 23) else "-23" 
                enddate += str(y) 
                enddate += "-10" if (d < 23) else "-11" 
                enddate += "-22" if (d < 23) else "-21"            
            elif(m == 10):
                startdate += str(y) 
                startdate += "-10" if (d < 23) else "-11" 
                startdate += "-23" if (d < 23) else "-22" 
                enddate += str(y) 
                enddate += "-11" if (d < 23) else "-12" 
                enddate += "-21" if (d < 23) else "-21"            
            elif(m == 11):
                startdate += str(y) 
                startdate += "-11" if (d < 22) else "-12" 
                startdate += "-22" if (d < 22) else "-22" 
                enddate += str(y) 
                enddate += "-12" if (d < 22) else "-01" 
                enddate += "-21" if (d < 22) else "-20"
            elif(m == 12):
                startdate += str(y) 
                startdate += "-12" if (d < 22) else "-01" 
                startdate += "-22" if (d < 22) else "-21"
                enddate += str(y) 
                enddate += "-01" if (d < 22) else "-02" 
                enddate += "-20" if (d < 22) else "-19"             

                
            tmp1 = Resturaunt_Employee_Day_Meal.objects.filter(
                resturaunt_day_meal__date__gte=startdate, 
                resturaunt_day_meal__date__lte=enddate).exclude(
                employee__department__exact=None).exclude(
                employee__department__exact=18).values('employee').annotate(
                selectedNo=Count('employee'),
                id=F('employee__id')).values_list('id')

            result1 = Employee.objects.filter(is_active__exact=1).exclude(
                department__exact=None).exclude(
                department__exact=18).exclude(
                id__in=tmp1).exclude(
                id__in=(1, 1689, 1471, 1616)).annotate(
                section=F('department__name')).values(
                'id', 'first_name', 'last_name', 'phone', 'section')
            
            tmp2 = Resturaunt_Employee_Day_Meal.objects.filter(
                resturaunt_day_meal__date__gte=startdate, 
                resturaunt_day_meal__date__lte=enddate).exclude(
                employee__project__exact=None).values('employee').annotate(
                selectedNo=Count('employee'),
                id=F('employee__id')).values_list('id')

            result2 = Employee.objects.filter(is_active__exact=1).exclude(
                project__exact=None).exclude(
                id__in=tmp2).annotate(
                section=F('project__name')).values(
                'id', 'first_name', 'last_name', 'phone', 'section')

            result = result1.union(result2).order_by('section')
            return Response(result)
        except Exception as ex:
            return Response('error: ', ex)   

class Resturaunt_Section_NamesViewAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    def get(self, request, *args, **kwargs):
        try:
            result = Department.objects.exclude(id__exact=18).values('name')
            result1 = Project.objects.values('name')
            result = result.union(result1)

            return Response(result)
        except Exception as ex:
            return Response('error: ', ex)
