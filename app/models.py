from django.db import models

# Create your models here.


class School(models.Model):
    sname=models.CharField(max_length=150)
    pname=models.CharField(max_length=150)
    locname=models.CharField(max_length=150)