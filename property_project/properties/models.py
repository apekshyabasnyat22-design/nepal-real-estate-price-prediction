from django.db import models

from django.db import models


class Property(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

    price = models.BigIntegerField()

    bedroom = models.IntegerField(null=True, blank=True)
    bathroom = models.IntegerField(null=True, blank=True)
    floors = models.IntegerField(null=True, blank=True)
    parking = models.IntegerField(null=True, blank=True)

    face = models.CharField(max_length=50, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)

    area = models.FloatField(null=True, blank=True)
    road = models.CharField(max_length=100, null=True, blank=True)
    road_width = models.FloatField(null=True, blank=True)
    road_type = models.CharField(max_length=100, null=True, blank=True)

    build_area = models.FloatField(null=True, blank=True)

    posted = models.CharField(max_length=100, null=True, blank=True)
    amenities = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
