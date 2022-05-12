from django.db import  models
from django.core.validators import MinLengthValidator

class Designer(models.Model):
    DesignerId = models.IntegerField(blank=False, unique=True, primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    contactnumber = models.CharField(max_length=12, blank=False)
    designeremailid = models.EmailField(blank=False)
    password = models.CharField(max_length=30, blank=False)

    
