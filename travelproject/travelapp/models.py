from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Client(models.Model):
    cname = models.CharField(max_length=250)
    cimg = models.ImageField(upload_to='picture')
    cdesc = models.TextField()

    def __str__(self):
        return self.cname
