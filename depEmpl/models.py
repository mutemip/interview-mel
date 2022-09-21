from django.db import models

# Create your models here.
import datetime

from django.db import models

class Department(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    dept_name = models.CharField(max_length=20, unique=True)

    def _str_(self):
        return self.dept_name

class Employee(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=10)
    emp_name = models.CharField(max_length=30)
    emp_dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    emp_salary = models.FloatField()
    doj = models.DateField()
    emp_address = models.TextField()

    def _str_(self):
        return self.emp_name
