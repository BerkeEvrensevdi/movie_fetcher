from django.db import models

from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.conf import settings
from decimal import Decimal


class Genre(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Person(models.Model):
    id_unique = models.IntegerField(unique=True)
    birth_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=10,default ="")
    biography = models.CharField(max_length=1000,default ="")
    name = models.CharField(max_length=50)
    portrait = models.ImageField(null=True, blank=True)
    portrait_url = models.URLField(max_length=250, blank=True)
    type = models.CharField(max_length=20,default ="")
    def __str__(self):
        return self.name


class Movie(models.Model):
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    date = models.DateField(default="")
    imdb = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    topic = models.CharField(max_length=1000, default ="")
    poster = models.ImageField(null=True, blank=True)
    poster_url = models.URLField(max_length=250, blank=True)
    poster_big_url = models.URLField(max_length=250, blank=True)
    #avg_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],default=0)
    avg_score = models.DecimalField(max_digits=2, decimal_places=1, default=Decimal(0.0),
                                validators=[MinValueValidator(0), MaxValueValidator(5.0)])
    genres = models.ManyToManyField(Genre, blank=True, related_name='movies')
    starring = models.ManyToManyField(Person, blank=True, related_name='stars')
    director = models.ManyToManyField(Person, blank=True, related_name='directors')
    writer = models.ManyToManyField(Person, blank=True, related_name='writers')
    video_url = models.URLField(max_length=250, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title




class Score(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    score = models.DecimalField(max_digits=2, decimal_places=1, default=Decimal(0.0),validators=[MinValueValidator(0), MaxValueValidator(5.0)])

    class Meta:
        unique_together = ('movie', 'user',)

class MovieHolder(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True)

class Post(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name = 'post_likes')
    is_liked = models.BooleanField(default=False)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text

    def total_likes(self):
        return self.likes.count()

    def get_bool(self,user):
        if self.likes.filter(id=user.id).exists():
            self.is_liked = True

        else:
            self.is_liked = False

        return self.is_liked








"""    
class profile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=12, blank=True, null=True)
    use_gravatar = models.BooleanField(default=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    avatar_url = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
"""