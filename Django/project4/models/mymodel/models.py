from django.db import models

# Create your models here.
class Mymodel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    desc=models.CharField(max_length=50)
