from django.db import models

# Create your models here.
class PortfolioPiece(models.Model):
    #id = models.IntegerField(unique=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    # if I change this to /static instead, I can get rid of the / in front of the url that is in the index
    image = models.ImageField(upload_to='static/img/haydensPortfolioPieces', verbose_name='My Photo', null=True, blank=False)

    modalDescription = models.CharField(max_length=1028, default="")
    modalProjectDescription = models.CharField(max_length=256, default="")
    # if I change this to /static instead, I can get rid of the / in front of the url that is in the index
    modalImage = models.ImageField(upload_to='static/img/haydensPortfolioPieceModals', verbose_name='Modal photo', null=True,blank=False)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name
