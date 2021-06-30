from django.contrib import admin
from .models import *


class MovieImageInline(admin.TabularInline):
    model = MovieShots
    max_num = 2
    min_num = 1


admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
