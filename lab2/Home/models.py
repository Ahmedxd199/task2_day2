from django.db import models

class Register(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)