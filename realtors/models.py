from django.db import models
from datetime import datetime

# Create your models here.
class Realtors(models.Model):
    name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/')
    desc=models.TextField(blank=True)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    hire_date=models.DateTimeField(default=datetime.now)
    is_mvp=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
