from django.urls import path, re_path

from . import views
from film.views import DetailView, IndexView, UpdateScoreView, UpdatePostView, GenreView, PersonView,Ratings,Recommend
app_name = 'film'
urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^movie_genre/(?P<genre_id>[\w ]+)/$', GenreView.as_view(), name='movie_genre'),
    re_path(r'^person_detail/(?P<person_id>[\w ]+)/$', PersonView.as_view(), name='person_detail'),
    re_path(r'^movie_detail/(?P<movie_id>[\w ]+)/$', DetailView.as_view(), name='movie_detail'),
    re_path(r'^ratings/$', Ratings.as_view(), name='ratings'),
    re_path(r'^recommend/$', Recommend.as_view(), name='recommend'),
    re_path(r'^update_score/(?P<movie_id>[\w ]+)/$', UpdateScoreView.as_view(), name='update_score'),
    re_path(r'^update_post/(?P<movie_id>[\w ]+)/$', UpdatePostView.as_view(), name='update_post'),
    re_path(r'^like/$', views.like_post, name='like_post'),
    re_path(r'^load_genres/$', views.load_genres, name='load_genres')

    #re_path(r'^post_detail/(?P<post_id>[\w ]+)/$', views.post_detail(), name='post_detail'),

    #re_path(r'^(?P<movie_id>[\w ]+)/$', PostView.as_view(), name='post'),
]