from django.db import models
from baseInfo.models import Employee
from datetime import datetime



class Library_Book_Type(models.Model):
    name = models.CharField(max_length=100)

    objects = models.Manager()  

    class Meta:
        db_table = "tbl_library_book_type"

class Library_Book_Publisher(models.Model):
    name = models.CharField(max_length=100)

    objects = models.Manager()  

    class Meta:
        db_table = "tbl_library_book_publisher"

class Library_Book_Author(models.Model):
    name = models.CharField(max_length=100)

    objects = models.Manager()  

    class Meta:
        db_table = "tbl_library_book_author"

class Library_Book(models.Model):
    name = models.CharField(max_length=100)
    code = models.PositiveSmallIntegerField()
    publisher = models.ForeignKey(Library_Book_Publisher, 
        related_name="book_publisher", on_delete=models.CASCADE)
    type = models.ForeignKey(Library_Book_Type, 
        related_name="book_type", on_delete=models.CASCADE)
    author = models.ForeignKey(Library_Book_Author, 
        related_name="book_author", on_delete=models.CASCADE)
    last_publish_date = models.DateField(default=datetime.now, blank=True)
    objects = models.Manager()  

    class Meta:
        db_table = "tbl_library_book"     

class Library_Loaned_Book(models.Model):
    date = models.DateField(default=datetime.now, blank=True)
    book = models.ForeignKey(Library_Book, 
        related_name="loaned_book", on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, 
        related_name="employee_borrowed_book", on_delete=models.CASCADE)
    objects = models.Manager()  

    class Meta:
        db_table = "tbl_library_loaned_book"