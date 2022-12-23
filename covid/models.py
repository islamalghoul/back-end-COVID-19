from django.db import models
class Covid(models.Model):
    Country=models.CharField(max_length=255,default="Jordan")
    total_confirmed_cases=models.CharField(max_length=255)
    total_deaths_cases=models.CharField(max_length=255)
    total_recovered_cases=models.CharField(max_length=255)
    Date=models.DateTimeField(auto_now_add=False) 
    
    
    def __str__(self):
        return self.total_confirmed_cases
# Create your models here.
