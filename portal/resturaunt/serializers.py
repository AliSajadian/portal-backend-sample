from django.db import models
from rest_framework import serializers

from resturaunt.models import Resturaunt_Meal, Resturaunt_Day_Meal, Resturaunt_Employee_Day_Meal, Resturaunt_Guest_Day_Meal
from baseInfo.models import Company, Department, Employee


class Resturaunt_MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resturaunt_Meal
        fields = '__all__'

class Resturaunt_Day_MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resturaunt_Day_Meal
        fields = '__all__'

class Resturaunt_Day_MealExSerializer(serializers.ModelSerializer):
    # resturaunt_meal = Resturaunt_MealSerializer()
    selectedNo = serializers.IntegerField()    

    class Meta:
        model = Resturaunt_Day_Meal
        fields = ('id', 'date', 'totalNo', 'resturaunt_meal', 'selectedNo')

class Resturaunt_MealBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resturaunt_Meal
        fields = 'name'

class Resturaunt_Served_MealSerializer(serializers.ModelSerializer):
    # resturaunt_meals = Resturaunt_MealBriefSerializer()

    resturaunt_meal = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    meal_no = serializers.IntegerField()
    selectedNo = serializers.IntegerField()    
    servedNo = serializers.IntegerField()  

    class Meta:
        model = Resturaunt_Day_Meal
        fields = ('meal_no', 'resturaunt_meal', 'totalNo', 'selectedNo', 'servedNo')        

# =======================================================
class CompanyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name')
        
class DepartmentBriefSerializer(serializers.ModelSerializer):
    # company = CompanyNameSerializer()
    company = serializers.SlugRelatedField(
        read_only=True,
        slug_field='company'
    )
    class Meta:
        model = Department
        fields = ('company')

class EmployeeBriefSerializer(serializers.ModelSerializer):
    department = DepartmentBriefSerializer(many=True)
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'personel_code', 'department')

class Resturaunt_Day_Meal_NamewSerializer(serializers.ModelSerializer):
    resturaunt_meal = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Resturaunt_Day_Meal
        fields = ('resturaunt_meal')  

class Resturaunt_Fish_MealSerializer(serializers.ModelSerializer):
    employee = EmployeeBriefSerializer(many=True)
    resturaunt_day_meal = Resturaunt_Day_Meal_NamewSerializer()
    # resturaunt_meal = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='resturaunt_meal'
    # )

    meal_no = serializers.IntegerField()

    class Meta:
        model = Resturaunt_Employee_Day_Meal
        fields = ('meal_no', 'resturaunt_day_meal', 'employee')   
# =======================================================
class Resturaunt_Employee_Day_MealSerializer(serializers.ModelSerializer):
    resturaunt_meal = serializers.SlugRelatedField(
        read_only=True,
        slug_field='resturaunt_meal'
     )
    date = serializers.SlugRelatedField(
        read_only=True,
        slug_field='date'
     )
    class Meta:
        model = Resturaunt_Employee_Day_Meal
        fields = ('id', 'employee', 'resturaunt_day_meal', 'resturaunt_meal', 'date')

class Resturaunt_Employee_Day_MealExSerializer(serializers.ModelSerializer):
    resturaunt_day_meal = Resturaunt_Day_MealSerializer()

    class Meta:
        model = Resturaunt_Employee_Day_Meal
        fields = ('id', 'employee', 'resturaunt_day_meal')


class Resturaunt_Guest_Day_MealSerializer1(serializers.ModelSerializer):
    resturaunt_meal = serializers.SlugRelatedField(
        read_only=True,
        slug_field='resturaunt_meal'
    )
    date = serializers.SlugRelatedField(
        read_only=True,
        slug_field='date'
    )
    class Meta:
        model = Resturaunt_Guest_Day_Meal
        fields = ('id', 'employee', 'resturaunt_day_meal', 'resturaunt_meal', 'date')

class Resturaunt_Guest_Day_MealExSerializer(serializers.ModelSerializer):
    resturaunt_meal = serializers.SlugRelatedField(
        read_only=True,
        slug_field='resturaunt_meal'
    )

    class Meta:
        model = Resturaunt_Guest_Day_Meal
        fields = ('id', 'date', 'resturaunt_meal', 'totalNo')        

class Resturaunt_Guest_Day_MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resturaunt_Guest_Day_Meal
        fields = '__all__'
        
    # id = serializers.IntegerField()
    # employee = serializers.IntegerField()
    # resturaunt_day_meal = serializers.IntegerField()
    # resturaunt_meal = serializers.IntegerField()
    # date = serializers.DateField(format="%Y-%m-%d")

    # resturaunt_meal = serializers.SerializerMethodField()
    # date = serializers.SerializerMethodField()

    # @classmethod
    # def get_resturaunt_meal(self, object):
    #     """getter method to add field retrieved_time"""
    #     return None

    # @classmethod
    # def get_date(self, object):
    #     """getter method to add field retrieved_time"""
    #     return None

    # class Meta:
    #     model = Resturaunt_Employee_Day_Meal
    #     fields = ('id', 'employee', 'resturaunt_day_meal', 'resturaunt_meal', 'date')     

    # id = serializers.PrimaryKeyRelatedField(read_only=True)
    # resturaunt_meal = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='resturaunt_meal'
    #  )
    # date = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='date'
    #  )
    # class Meta:
    #     model = Resturaunt_Employee_Day_Meal
    #     fields = ('employee', 'resturaunt_day_meal', 'resturaunt_meal', 'date')