from django.contrib.gis.db import models



class GrantReference(models.Model):
    grant_id = models.CharField(max_length=6)
    name = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    financial_year = models.IntegerField()

    def __str__(self):
        return self.name

class SiteOutline(models.Model):
    grant_id = models.ForeignKey(GrantReference, on_delete=models.CASCADE)
    name = models.TextField()
    geom = models.PolygonField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Site outlines"

class RestorationLines(models.Model):
    CHOICES = (
        (1, 'Peat dam'),
        (2, 'Hag reprofiling'),
        (3, 'Gully reprofiling'),
    )
    site_id = models.ForeignKey(SiteOutline, on_delete=models.CASCADE)
    technique = models.IntegerField(choices=CHOICES)
    geom = models.LineStringField()

    class Meta:
        verbose_name_plural = "Restoration lines"


class RestorationPoints(models.Model):
    CHOICES = (
        (1, 'Peat dam'),
        (2, 'Gully block')
    )
    site_id = models.ForeignKey(SiteOutline, on_delete=models.CASCADE)
    technique = models.IntegerField(choices=CHOICES)
    geom = models.PointField()

    class Meta:
        verbose_name_plural = "Restoration points"
