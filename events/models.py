from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name