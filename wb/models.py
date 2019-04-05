from django.db import models

# Create your models here.

class user_info(models.Model):
	student_id 	=models.CharField(primary_key=True,max_length=20)
	name		=models.CharField(max_length=20)
	phone		=models.CharField(max_length=100)
	idCard		=models.CharField(max_length=100)
	bankCard	=models.CharField(max_length=100)


class user_info_update(models.Model):
	student_id  = models.CharField(primary_key=True,max_length=50)
	home_addr	= models.CharField(max_length=300)
	mother_phone= models.CharField(max_length=50)
	father_phone= models.CharField(max_length=50)


class user_account(models.Model):
	student_id = models.CharField(primary_key=True,max_length=20)
	student_pwd= models.CharField(max_length=50)
