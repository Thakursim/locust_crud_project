from django.db import models

# Create your models here.
class FillNumbers(models.Model):
    number_1 = models.IntegerField()
    number_2 = models.IntegerField()
    number_3 = models.IntegerField()
    text_4 = models.CharField(max_length=10)
    

class CoderHome(models.Model):
    developer = models.CharField(max_length=20)
    tester = models.CharField(max_length=20)
    infra_dev = models.IntegerField()
