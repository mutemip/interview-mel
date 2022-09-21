from django.urls import path
from . import views

urlpatterns = [
    path("", views.emp_join_date, name='joindate'),
    path('deptname', views.emp_dept_name, name='deptname'),
    path('empsalary', views.emp_salary, name='empsalary'),
    path('empdeptname', views.emp_name_dept, name='empdeptname')
]