from django.db import models


class Motorcade(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)


class Fleetleader(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    sex = models.BooleanField()
    hasfleet = models.CharField(max_length=255)


class Road(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    belongs = models.CharField(max_length=255)


class Driver(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    is_roadleader = models.BooleanField(default=False)
    sex = models.BooleanField()
    belongs = models.CharField(max_length=255)


class Motors(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    seats = models.IntegerField(default=4)


class Punishment(models.Model):
    ID = models.AutoField(primary_key=True)
    drivername = models.CharField(max_length=255)
    driverID = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    carID = models.CharField(max_length=255)
    station = models.CharField(max_length=255)
    time = models.DateTimeField()
    belongs = models.CharField(max_length=255)


# 用于统计类别的类，不需要创建数据库
class types:
    def __init__(self):
        self.type=None
        self.number=0