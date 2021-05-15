from django.contrib import admin

from .models import Movie,Score,Post,Genre,Person

admin.site.register(Movie)

admin.site.register(Score)
admin.site.register(Post)
admin.site.register(Genre)
admin.site.register(Person)