from django.db import models


class Register(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    Intakeid = models.ForeignKey('Intake', on_delete=models.CASCADE)


class Intake(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)

