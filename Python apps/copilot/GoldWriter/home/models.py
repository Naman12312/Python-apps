from djongo import models

# Create your models here.
class Prompt(models.Model):
    
    pro = models.TextField()
    role = models.CharField(max_length=10)
    response = models.TextField()