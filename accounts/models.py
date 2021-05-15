from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from film.models import Score, Post, MovieHolder
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    spec_id = models.CharField(max_length=200, unique=True, default='')
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100,default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default = 0)
    scores = models.ManyToManyField(Score, blank=True, related_name='ratings')
    posts = models.ManyToManyField(Post, blank=True, related_name='posts')
    recommended_movies = models.ManyToManyField(MovieHolder, blank=True, related_name='rec_movies')

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])



post_save.connect(create_profile, sender = User)