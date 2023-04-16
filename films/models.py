from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

