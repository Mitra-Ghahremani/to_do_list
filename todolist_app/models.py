from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Task(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    description=models.TextField(max_length=150,null=True,blank=True)
    datetime_start=models.DateTimeField(null=True,blank=True)
    datetime_end=models.DateTimeField(null=True,blank=True)
    situation=models.BooleanField(default=False)
    

    def __str__(self):
        return self.title