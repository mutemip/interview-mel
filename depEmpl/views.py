from django.shortcuts import render
from .models import Employee, Department

# Create your views here.
def emp_join_date(date):
    return Employee.objects.filter(doj__date=date)

def emp_dept_name(dept_name):
    return Employee.objects.filter(emp_dept__dept_name=dept_name)

def emp_salary(salary1, salary2):
    return Employee.objects.filter(emp_salary_gte=salary1, emp_salary_lte=salary2)

def emp_name_dept(name, dept_name):
    return Employee.objects.filter(emp_name=name, emp_dept__dept_name=dept_name)