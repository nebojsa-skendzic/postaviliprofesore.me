from django.db import models
# Create your models here.


class UpdatedFiles(models.Model):
    title = models.TextField()
    link = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    subjecttag = models.TextField()
    webtag = models.TextField(default=None)  # The base url to search from

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Updated Files"


class Fakultet(models.Model):
    fakultet = models.CharField(max_length=120)

    def __str__(self):
        return self.fakultet


class Smjer(models.Model):
    fakultet = models.ForeignKey('Fakultet', on_delete=models.CASCADE)
    smjer = models.CharField(max_length=120)

    def __str__(self):
        return self.smjer


class Semestar(models.Model):
    fakultet = models.ForeignKey('Fakultet', on_delete=models.CASCADE)
    smjer = models.ForeignKey('Smjer', on_delete=models.CASCADE)
    semestar = models.IntegerField()
    resultlink = models.TextField()

    def __str__(self):
        return self.smjer.smjer + ", " + str(self.semestar) + ". semestar"
