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

def emp_join_date(date):
    return Employee.objects.filter(doj__date=date)

def emp_dept_name(dept_name):
    return Employee.objects.filter(emp_dept__dept_name=dept_name)

def emp_salary(salary1, salary2):
    return Employee.objects.filter(emp_salary_gte=salary1, emp_salary_lte=salary2)

def emp_name_dept(name, dept_name):
    return Employee.objects.filter(emp_name=name, emp_dept__dept_name=dept_name)