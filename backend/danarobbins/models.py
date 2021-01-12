from django.db import models

# Create your models here.
class Gigs(models.Model):
    venue = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    artist_name = models.CharField(max_length=50)

    def __str__(self):
        return self

