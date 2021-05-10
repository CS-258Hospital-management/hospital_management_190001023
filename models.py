from django.db import models

# Create your models here.

class pharm(models.Model):  
    Medicine_Id = models.IntegerField()  
    Medicine_Name = models.CharField(max_length=50)  
    Stock_Left = models.IntegerField() 
    Last_updated = models.DateField()
  

class billing(models.Model):  
    userid = models.IntegerField()  
    date = models.DateField()  
    amount = models.CharField(max_length=10) 