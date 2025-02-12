from django.db import models

# Create your models here.
class Marvel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    heroic_name = models.CharField(max_length=50)

   