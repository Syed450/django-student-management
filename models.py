from django.db import models
class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField()
   
    def __str__(self):
        return self.email 

# Create your models here.
