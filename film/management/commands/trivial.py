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


        #file1 = open('film/management/commands/Attributes_Imdb_test1', 'r')
        #Lines = file1.readlines()
        imdb_id_list = []

        f = open("film/management/commands/recommendedfilm")
        recommend = {}
        for i in f:
            l = i.split("\n")[0].split("\t")
            recommend[l[0]] = eval(l[1])


        """
        for line in Lines:
            k = line.split('\t')[0]
            imdb_id_list.append(k)
        """
        for user_id in recommend.keys():
            k = "user id = %s" % user_id
            print(k)
            user_profile = UserProfile.objects.get(spec_id=user_id)
            print(user_profile)
            printed = '********************User ID %d is found********************' % user_count
            print(printed)
            user_count = user_count+1

