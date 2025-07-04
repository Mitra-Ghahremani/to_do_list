from django.db import models



class Task(models.Model):
    title=models.CharField(max_length=20,null=True,blank=True)
    description=models.TextField(max_length=150,null=True,blank=True)
    datetime_start=models.DateTimeField(null=True,blank=True)
    datetime_end=models.DateTimeField(null=True,blank=True)
    situation=models.BooleanField(default=False)