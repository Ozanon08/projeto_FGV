from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    cover_image = models.ImageField(upload_to='movie_covers/',null=True)
    trailer_url = models.URLField(blank=True, null=True)
    is_favorite = models.BooleanField(default=False)
    watched = models.BooleanField(default=False)
    watched_by_users = models.ManyToManyField(User, related_name='watched_movies', blank=True)
    favorite_of_users = models.ManyToManyField(User, related_name='favorite_movies', blank=True)

    def __str__(self):
        return self.title
