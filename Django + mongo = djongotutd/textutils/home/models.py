from django.db import models

# Create your models here.
class Remain(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()


    