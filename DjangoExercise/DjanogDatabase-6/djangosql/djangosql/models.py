from django.db import connections
from django.db import models  
class Employee(models.Model):  
    eid      = models.CharField(max_length=20)      
    ename    = models.CharField(max_length=100) 
    eemail   = models.CharField(max_length=50) 
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"  