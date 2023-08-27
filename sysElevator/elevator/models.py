from django.db import models

class Elevator(models.Model):
    operational = models.BooleanField(default=True)
    current_floor = models.IntegerField(default=1)
    moving_up = models.BooleanField(default=True)
    doors_open = models.BooleanField(default=False)
    # Other fields and methods as needed

class Request(models.Model):
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    floor = models.IntegerField()
    direction = models.CharField(max_length=4)  # 'up' or 'down'
    completed = models.BooleanField(default=False)
