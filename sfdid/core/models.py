from django.db import models

# Create your models here.
class CollegeAdmission(models.Model):
    name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)

    def __str__(self):
        return self.last_name