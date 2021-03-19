from django.db import models
# Create your models here.


class UpdatedFiles(models.Model):
    webtag = models.TextField(default=None)  # The base url to search from
    sitedata = models.JSONField()

    def __str__(self):
        return self.webtag

    class Meta:
        verbose_name_plural = "Updated Files"


class Fakultet(models.Model):
    fakultet = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Fakulteti"

    def __str__(self):
        return self.fakultet


class Smjer(models.Model):
    smjer = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Smjerovi"

    def __str__(self):
        return self.smjer


class Semestar(models.Model):
    smjer = models.ForeignKey('Smjer', on_delete=models.CASCADE)
    fakultet = models.ForeignKey('Fakultet', on_delete=models.CASCADE)
    semestar = models.IntegerField()
    resultlink = models.TextField()

    def __str__(self):
        return self.smjer.smjer + ", " + str(self.semestar) + ". semestar"
