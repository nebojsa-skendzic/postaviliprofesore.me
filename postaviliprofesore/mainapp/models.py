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
