from django.db import models

# Create your models here.
class Gigs(models.Model):
    venue = models.CharField(max_length=50, default='')
    time = models.DateTimeField(auto_now=False, auto_now_add=False, default='')
    artist_name = models.CharField(max_length=50, default='')
    ticket_link = models.URLField(("Concert Link"), max_length=200)

    def __str__(self):
       return self.artist_name

