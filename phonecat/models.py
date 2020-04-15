from django.db import models

# Create your models here.
class PhonesTab(models.Model):
    Name = models.CharField(max_length=255)
    RegDate = models.DateTimeField('date published')
    Address = models.CharField(max_length=255)
    Phone = models.CharField(max_length=30)


