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


        f = open("film/management/commands/watchedfilms")
        watchedfilms = {}
        for i in f:
            l = i.split("\n")[0].split("\t")
            watchedfilms[l[0]] = eval(l[1])

        for user_id in watchedfilms.keys():

            films = watchedfilms[user_id]


            my_user = User.objects.get(username=user_id)
            user_profile = UserProfile.objects.get(spec_id=user_id)
            printed = 'User ID = %d and Username = %s is got' % (user_count, user_id)
            print(printed)
            user_count = user_count + 1

            for film in films:  # film[0] = imdb_id  ve film[1] = user_score

                imdb_id = film[0]
                user_score = Decimal(film[1])



                control_exist = Mov.objects.filter(imdb=imdb_id)

                if control_exist:
                    my_movie = Mov.objects.get(imdb=imdb_id)
                    score = Score(user=my_user, movie=my_movie, score=user_score)
                    try:
                        score.save()
                    except:
                        print("You can not assign a score to movie with this user. Because this user already assign a score this movie")
                        score = Score.objects.filter(user=my_user, movie=my_movie).update(score=user_score)
                        print("So same score is updated only")
                        continue
                    user_profile.scores.add(score)
                    user_profile.save()
                else:
                    alert = "The movie %s not in db" % imdb_id
                    print(alert)




        self.stdout.write(self.style.SUCCESS('Successfully added'))
