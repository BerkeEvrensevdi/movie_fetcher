
from .models import Score,Movie,Post,Genre,Person
from django.http import HttpResponse, HttpResponseRedirect,Http404,JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import View,ListView,FormView
from film.forms import DetailForm,PostForm
from django.shortcuts import render
from django.template.loader import render_to_string
from django.db.models import Q
from accounts.models import UserProfile
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

import json
"""
class IndexView(View):
    template_name ='film/index.html'
    

    def get(self,request):
        movie_list = Movie.objects.all()
        return render(request, self.template_name, {'movie_list':movie_list})

    

    def get_queryset(self,request):
        query = self.request.GET.get('q')
        if query:
            return Movie.objects.filter(title__icontains=query)
        else:
            return Movie.objects.all()      
"""
class Ratings(ListView):
    template_name = 'film/ratings.html'

    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        scores = user_profile.scores.all()

        return render(request, self.template_name, {'scores': scores})


class Recommend(ListView):
    template_name = 'film/recommend.html'

    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)

        rec_movies = user_profile.recommended_movies.all()


        return render(request, self.template_name, {'rec_movies': rec_movies})


def load_genres(request):
    #genre = get_object_or_404(Genre, id=request.GET.get('genre_id'))
    genre_name= request.GET.get('genre_name')
    fromyear = request.GET.get('fromyear')
    toyear = request.GET.get('toyear')



    if genre_name != '' and fromyear != '' and toyear == '':
        movies = Movie.objects.filter(genres__name__contains=genre_name, year__gte=fromyear)
    elif genre_name != '' and toyear != '' and fromyear == '':
        movies = Movie.objects.filter(genres__name__contains=genre_name, year__lte=toyear)
    elif fromyear != '' and toyear != '' and genre_name == '':
        movies = Movie.objects.filter(year__gte=fromyear, year__lte=toyear)
    elif toyear != '' and fromyear == '' and genre_name == '':
        movies = Movie.objects.filter(year__lte=toyear)
    elif fromyear != '' and toyear == '' and genre_name == '':
        movies = Movie.objects.filter(year__gte=fromyear)
    elif genre_name != '' and toyear == '' and fromyear == '':
        movies = Movie.objects.filter(genres__name__contains=genre_name)
    elif genre_name != '' and fromyear != '' and toyear != '':
        movies = Movie.objects.filter(genres__name__contains=genre_name, year__gte=fromyear, year__lte=toyear)
    #movies = Movie.objects.filter(genres=genre,year__gte=fromyear, year__lte=toyear)


    context = {'movies': movies}
    if request.is_ajax():
        html = render_to_string('film/genre_dropdown_list_options.html', context, request=request)
        return JsonResponse({'form':html})




class GenreView(ListView):
    template_name = 'film/movie_genre.html'

    def get(self, request,genre_id):
        genre = get_object_or_404(Genre, pk=genre_id)
        movies = Movie.objects.filter(genres=genre)
        return render(request, self.template_name, {'movies': movies})

"""
class GenreListView(ListView):
    model = Movie
    template_name = 'film/index.html'

    def get_queryset(self):
        movies = Movie.objects.all()
        query = self.request.GET.get('genre', None)
        if query:
           return movies.filter(genre=query)
        return movies
"""

class IndexView(ListView):
    template_name = 'film/index.html'
    context_object_name = 'movies'
    model = Movie
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'genres': Genre.objects.all().order_by('name'),
            'page_title': 'Latest'
        })
        return context


    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Movie.objects.filter(title__icontains=query)
        else:
            return Movie.objects.all()





class PersonView(View):
    template_name = 'film/person_detail.html'

    def get(self, request, person_id):
        person = get_object_or_404(Person, pk=person_id)
        movies = Movie.objects.filter(Q(starring=person)| Q(writer=person) | Q(director=person)).distinct()


        return render(request, self.template_name,{'movies':movies, 'person':person})


"""
def detail(request,movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'film/detail.html', {'movie': movie})
"""



"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import MyForm

class MyFormView(View):
    form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
"""
"""
      if form_post.is_valid():
          post = form_post.save(commit=False)
          post.user = request.user
          post.movie_id = movie_id
      """
"""


"""
"""
def like_users(request):


    post = get_object_or_404(Post, id =request.POST.get('post_id'))


    context = {
               'post': post,
               'message':message
               }

    if request.is_ajax():
        html = render_to_string('film/like-section.html', context, request=request)
        return JsonResponse({'form':html})
"""
def like_post(request):

    user = request.user
    post = get_object_or_404(Post, id =request.POST.get('post_id'))

    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user)
        post.is_liked = False

    else:
        post.likes.add(user)
        post.is_liked = True

    message = post.likes.all()

    context = {'total_likes':post.total_likes(),
               'post': post,
               'message': message,
               }

    if request.is_ajax():
        html = render_to_string('film/like-section.html', context, request=request)
        return JsonResponse({'form':html})
"""
def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False

    else:
        post.likes.add(request.user)
        is_liked = True

    context = {
        'post' : post,
        'is_liked' : is_liked,
        'total_likes' : post.total_likes(),
    }

    if request.is_ajax():
        html = render_to_string('film/detail.html',context,request=request)
        return JsonResponse({'form':html})
    return HttpResponseRedirect(post.get_absolute_url())
"""

class UpdateScoreView(View):
    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        profile = get_object_or_404(UserProfile, user=request.user)
        form_score = DetailForm(request.POST)


        if form_score.is_valid():
            score = form_score.save(commit=False)
            score.user = request.user
            score.movie_id = movie_id
            score, created = Score.objects.update_or_create(
                movie=score.movie, user=score.user, defaults={'score': score.score}
            )
            profile.scores.add(score)

            tot_score = movie.avg_score * (len(movie.score_set.all()) - 1)
            tot_score += score.score
            avg = tot_score / len(movie.score_set.all())
            movie.avg_score = avg
            score.save()
            movie.save()
            return redirect('film:movie_detail', movie_id=movie_id)
        else:
            return redirect('film:movie_detail', movie_id=movie_id)

class UpdatePostView(View):
    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        profile = get_object_or_404(UserProfile, user=request.user)
        form_post = PostForm(request.POST)


        if form_post.is_valid():
            post = form_post.save(commit=False)
            post.author = request.user
            post.movie_id = movie_id
            post, created = Post.objects.update_or_create(
                movie=post.movie, author=post.author, defaults={'text': post.text}
            )
            post.text = form_post.cleaned_data['post']
            post.save()
            profile.posts.add(post)
            return redirect('film:movie_detail', movie_id=movie_id)
        else:
            return render(request, 'film/detail.html')


class DetailView(View):
    template_name ='film/detail.html'

    def get(self, request,movie_id):
        form_score = DetailForm()
        form_post = PostForm()
        movie = get_object_or_404(Movie, pk=movie_id)

        try:
            score = movie.score_set.get(user=request.user)
        except (KeyError, Score.DoesNotExist):
            score = None


        try:
            score_list = movie.score_set.all()
        except (KeyError, Score.DoesNotExist):
            score_list = None

        try:
            posts = Post.objects.filter(movie_id = movie_id)
        except (KeyError, Post.DoesNotExist):
            posts = None


        return render(request, self.template_name,{'score_list':score_list, 'score': score,'posts': posts, 'form_post':form_post, 'form_score': form_score, 'movie':movie})

"""
class PostFormView(FormView):
    form_class = PostForm()
    template_name = 'film/detail.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form_post = self.form_class(request.POST)
        form_score = DetailForm()
        if form_post.is_valid():
            form_post.save()
            return self.render_to_response(
                self.get_context_data(
                    success=True
                )
            )
        else:
            return self.render_to_response(
                self.get_context_data(
                    form_post=form_post,
                    form_score=form_score
                )
            )
"""
"""
class PostView(View):
    template_name ='film/detail.html'

    def get(self, request,movie_id):
        form_post = PostForm()
        movie = get_object_or_404(Movie, pk=movie_id)

        try:
            posts = Post.objects.get(movie_id = movie_id)
        except (KeyError, Post.DoesNotExist):
            return render(request, self.template_name, {'form_post': form_post, 'movie': movie})

        if posts:
            return render(request, self.template_name,{'form_post': form_post,'posts':posts})


    def post(self, request,movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        form_post = PostForm(request.POST)

        if form_post.is_valid():
            post = form_post.save(commit=False)
            post.user = request.user
            post.movie_id = movie_id

            post.save()
            text = form_post.cleaned_data['post']
            form_post = PostForm()

            args = {'form_post': form_post, 'post': post, 'movie': movie}

            return render(request, self.template_name, args)

        args = {'form_post': form_post, 'post': text, 'movie': movie}
        return render(request, self.template_name, args)
"""
"""
class DetailView(View):
    template_name ='film/detail.html'

    def get(self, request,movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        score = movie.score_set.get(user=request.user)
        posts = Post.objects.get(movie_id = movie_id)

            return render(request, self.template_name, {'posts': posts, 'score': score, 'movie': movie})

"""