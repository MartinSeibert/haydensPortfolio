from django.db import models

# Create your models here.
class PortfolioPiece(models.Model):
    #id = models.IntegerField(unique=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    imagePath = models.CharField(max_length=256)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name
