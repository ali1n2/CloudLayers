from django.db import models


# Create your models here.
class PSD(models.Model):
    file = models.FileField(upload_to="static/psd")
