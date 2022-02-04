from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Sum
from django.contrib.gis.db.models.functions import Area


'''class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username'''

class Grant(models.Model):
    reference = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='grants', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    financial_year = models.PositiveIntegerField()

    def site_area(self):
        areas = Grant.objects.annotate(area=Sum(Area('sites__geom')))
        return areas

    def __str__(self):
        return self.reference

    class Meta:
        verbose_name_plural = "Grants"
    

class Site(models.Model):
    grant_id = models.ForeignKey(Grant, related_name='sites', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    geom = models.PolygonField(blank=False, null=False, srid=27700)

    def get_hectares(self):
        return self.geom.area.sq_m/10000

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sites"

class RestorationLines(models.Model):
    CHOICES = (
        ('peat_dam', 'Peat dam'),
        ('hag_reprofling', 'Hag reprofiling'),
        ('gully_reprofiling', 'Gully reprofiling'),
        ('wave_dam', 'Wave dam'),
    )

    site = models.ForeignKey(Site, related_name='lines', on_delete=models.CASCADE)
    technique = models.CharField(choices=CHOICES, blank=False, null=False, max_length=100)
    geom = models.LineStringField(blank=False, null=False, srid=27700)

    class Meta:
        verbose_name_plural = "Restoration lines"


class RestorationPoints(models.Model):
    CHOICES = (
        ('peat_dam', 'Peat dam'),
        ('gully_block', 'Gully block'),
        ('stone_dam', 'Stone dam'),
        ('wooden_dam', 'Wooden dam')
    )

    site = models.ForeignKey(Site, related_name='points', on_delete=models.CASCADE)
    technique = models.CharField(choices=CHOICES, blank=False, null=False, max_length=100)
    geom = models.PointField(blank=False, null=False, srid=27700)

    class Meta:
        verbose_name_plural = "Restoration points"
