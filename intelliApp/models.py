from django.db import models

# Create your models here.
class Department(models.Model):
	id=models.CharField(primary_key=True,max_length=3)
	department=models.CharField(unique=True,max_length=15)
	class Meta:
		db_table="department"
	def _str_(self):
		return self.id

class Employee(models.Model):
	Emp_id=models.CharField(primary_key=True,max_length=3)
	Emp_name=models.CharField(max_length=20)
	Emp_Department=models.ForeignKey(Department,on_delete=models.CASCADE)
	Emp_salary=models.FloatField()
	DOJ=models.DateField()
	Emp_address=models.TextField()
	class Meta:
		db_table="employee"
	def _str_(self):
		return self.Emp_name