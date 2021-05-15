from django.core.management.base import BaseCommand, CommandError
from film.models import Movie as Mov,Person,Genre,Score
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth.models import User
from decimal import Decimal
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'


    def handle(self, *args, **options):

        not_added = 0
        added = 0
        mov_id = 1
        user_count = 1
        from tmdbv3api import TMDb

        tmdb = TMDb()

        tmdb.api_key = '' # api_key

        tmdb.language = 'en'
        tmdb.debug = True

        from tmdbv3api import Movie

        mov = Movie()

        #file1 = open('film/management/commands/Attributes_Imdb_test1', 'r')
        #Lines = file1.readlines()
        imdb_id_list = []
        """
        f = open("recommendedfilm")
        recommend = {}
        for i in f:
            l = i.split("\n")[0].split("\t")
            recommend[l[0]] = eval(l[1])
        """
        f = open("film/management/commands/watchedfilms")
        watchedfilms = {}
        for i in f:
            l = i.split("\n")[0].split("\t")
            watchedfilms[l[0]] = eval(l[1])
        """
        for line in Lines:
            k = line.split('\t')[0]
            imdb_id_list.append(k)
        """
        for user_id in watchedfilms.keys():

            films = watchedfilms[user_id]

            user_email = "user%d@hotmail.com" % user_count
            try:
                auth_user = User.objects.create_user(username=user_id, email=user_email, password='pass123')
            except:
                my_user = User.objects.get(username=user_id)
                user_profile = UserProfile.objects.create(user=my_user, spec_id=user_id)

            printed = 'User ID %d is added' % user_count
            print(printed)
            user_count = user_count + 1

            for film in films:  # film[0] = imdb_id  ve film[1] = user_score

                imdb_id = film[0]
                user_score = Decimal(film[1])



                control_exist = Mov.objects.filter(imdb=imdb_id)

                if control_exist:
                    my_movie = Mov.objects.get(imdb=imdb_id)
                    score = Score(user=my_user, movie=my_movie, score=user_score)
                    score.save()
                    user_profile.scores.add(score)
                    user_profile.save()

                else:

                    k = mov.details(imdb_id)

                    try:
                        m = k.poster_path
                        img_path = "https://image.tmdb.org/t/p/w185%s" % m
                        big_img_path = "https://image.tmdb.org/t/p/w500%s" % m
                    except:
                        error_id = "imdb id = %s can not be added" % imdb_id
                        print(error_id)
                        not_added = not_added+1
                        continue

                    try:
                        p = k.vote_average
                        vote_average = Decimal(p)
                        vote_average = vote_average/2
                        vote_average = round(vote_average, 1)

                    except:
                        vote_average = Decimal(0.0)


                    genre_list = []

                    if k.original_title:
                        title = k.original_title

                    if k.overview:
                        overview = k.overview

                    for genre in k.genres:
                        genre_list.append(genre)

                    vid = mov.videos(imdb_id)
                    key = ""
                    if vid:
                        key = vid[0].key

                    yt_url = "https://www.youtube.com/embed/%s" % key
                    rls_date = k.release_date
                    rls_year = k.release_date.split('-')[0]



                    credits = mov.credits(imdb_id)

                    cast_list = []
                    for c in credits.cast:
                        cast_list.append(c)

                    if cast_list:
                        print(cast_list[0]['name'])

                        for c in cast_list:
                            t = c['profile_path']
                            c['profile_path'] = "https://image.tmdb.org/t/p/w342%s" % t

                    writer_list = []
                    director_list = []
                    for c in credits.crew:
                        if c['department'] == "Writing":
                            writer_list.append(c)
                        if c['department'] == "Directing" and c['job'] == "Director":
                            director_list.append(c)

                    for c in writer_list:
                        t = c['profile_path']
                        c['profile_path'] = "https://image.tmdb.org/t/p/w342%s" % t

                    for c in director_list:
                        t = c['profile_path']
                        c['profile_path'] = "https://image.tmdb.org/t/p/w342%s" % t


                    movie = Mov(year=rls_year, date=rls_date, imdb=imdb_id, title=title,
                                topic=overview,poster_url=img_path,poster_big_url=big_img_path,
                                video_url=yt_url, avg_score=vote_average)
                    try:
                        movie.save()
                    except:
                        print("There is invalid field somewhere in movie fields. So this can not be added")
                        not_added = not_added + 1
                        continue

                    adding_control = "movie_id %d is added" % mov_id
                    print(adding_control)
                    mov_id = mov_id + 1

                    for i in cast_list:
                        person_query = Person.objects.filter(id_unique = i['id'])
                        if not person_query:
                            person = Person(id_unique=i['id'], name=i['name'], portrait_url=i['profile_path'], type='Star')
                            person.save()
                            movie.starring.add(person)
                            movie.save()
                        else:
                            person = Person.objects.get(id_unique = i['id'])
                            movie.starring.add(person)
                            movie.save()

                    for i in writer_list:
                        person_query = Person.objects.filter(id_unique=i['id'])
                        if not person_query:
                            person = Person(id_unique=i['id'], name=i['name'], portrait_url=i['profile_path'], type='Writer')
                            person.save()
                            movie.writer.add(person)
                            movie.save()
                        else:
                            person = Person.objects.get(id_unique=i['id'])
                            movie.writer.add(person)
                            movie.save()

                    for i in director_list:
                        person_query = Person.objects.filter(id_unique=i['id'])
                        if not person_query:
                            person = Person(id_unique=i['id'], name=i['name'], portrait_url=i['profile_path'], type='Director')
                            person.save()
                            movie.director.add(person)
                            movie.save()
                        else:
                            person = Person.objects.get(id_unique=i['id'])
                            movie.director.add(person)
                            movie.save()

                    for i in genre_list:

                        existing_genre = Genre.objects.filter(name__exact=i['name'])
                        if not existing_genre:
                            genre = Genre(name=i['name'])
                            genre.save()
                            movie.genres.add(genre)
                            movie.save()
                        else:
                            genre = Genre.objects.get(name=i['name'])
                            movie.genres.add(genre)
                            movie.save()

                    score = Score(user=my_user, movie=movie, score=user_score)
                    score.save()
                    user_profile.scores.add(score)
                    user_profile.save()
            """
            if user_count == 6:
                break
            """
        not_added_result = 'Eklenmeyen sayisi = %d' % not_added
        print(not_added_result)
        self.stdout.write(self.style.SUCCESS('Successfully added'))
