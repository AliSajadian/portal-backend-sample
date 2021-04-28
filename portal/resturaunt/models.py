from django.db import models
from datetime import datetime, date
from django.db.models import Count

from baseInfo.models import Department, Employee


class Resturaunt_Meal(models.Model):
    name = models.CharField(max_length=100)
    picture = models.FileField(upload_to='meal_pix', null=True)
    objects = models.Manager()  

    class Meta:
        db_table = "tbl_resturaunt_meal"

class Resturaunt_Day_Meal(models.Model):
    resturaunt_meal = models.ForeignKey(Resturaunt_Meal, 
        related_name="ResturauntMeal_ResturauntDayMeal", on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now, blank=True)
    totalNo = models.IntegerField(null=True)
    objects = models.Manager()  

    # def meal_no(self):
    #     currentdate = date.today()
    #     aggregate = Resturaunt_Day_Meal.objects.filter(date=currentdate, id__lte=self.id).aggregate(meal_no=Count('id'))
    #     return aggregate['meal_no']

    class Meta:
        unique_together = ('resturaunt_meal', 'date')
        db_table = "tbl_resturaunt_day_meal"

class Resturaunt_Employee_Day_Meal(models.Model):
    resturaunt_day_meal = models.ForeignKey(Resturaunt_Day_Meal, 
        related_name="ResturauntDayMeal_ResturauntEmployeeDayMeal", on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, 
        related_name="Employee_ResturauntEmployeeDayMeal", on_delete=models.CASCADE)
    served = models.BooleanField(default=False)
    objects = models.Manager()  

    class Meta:
        db_table = "tbl_resturaunt_employee_day_meal"  

class Resturaunt_Guest_Day_Meal(models.Model):
    department = models.ForeignKey(Department, 
        related_name="Department_ResturaunGuestDayMeal", on_delete=models.CASCADE, null=True)  
    resturaunt_day_meals=models.ManyToManyField(Resturaunt_Day_Meal, through='Resturaunt_Guest_Day_Meal_junction')
    # date = models.DateField(default=datetime.now, blank=True)
    description=models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = "tbl_resturaunt_guest_day_meal"  

class Resturaunt_Guest_Day_Meal_Junction(models.Model):
    resturaunt_day_meal = models.ForeignKey(Resturaunt_Day_Meal, 
        related_name="ResturauntDayMeal_ResturauntGuestDayMealJunction", on_delete=models.CASCADE)
    resturaunt_guest_day_meal = models.ForeignKey(Resturaunt_Guest_Day_Meal, 
        related_name="ResturauntGuestDayMeal_ResturauntGuestDayMealJunction", on_delete=models.CASCADE)
    qty = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = [['resturaunt_day_meal', 'resturaunt_guest_day_meal']]
        db_table = "tbl_resturaunt_guest_day_meal_junction"

