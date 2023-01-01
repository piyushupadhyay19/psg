from django.db import models

# makemigrations - create changes and store in a file
# migrate - apply the changes created by makemigrations

# Create your models here.
class Shipping(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=122)
    address2 = models.CharField(max_length=122)
    country = models.CharField(max_length=20)
    zip = models.CharField(max_length=6)
    ccName = models.CharField(max_length=122)
    ccNumber = models.CharField(max_length=19)
    ccExpiration = models.CharField(max_length=5)
    ccCvv = models.CharField(max_length=3)
    date = models.DateField()

    def __str__(self):
        return self.firstName + " " + self.lastName