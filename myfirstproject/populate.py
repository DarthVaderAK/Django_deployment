import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","myfirstproject.settings")
#for linking this .py file to django first_project

import django
django.setup()

#Fake pop JavaScript
import random
from first_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen=Faker()
topics=["search","social","marketplace","news","games"]

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]# [0] because get_or_create return tuple, selecting first element
    t.save()
    return t
def populate(N=5):
    for entry in range(N):
        #get a topic for entry
        top=add_topic()

        #create fake data for that entry

        fake_url = fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        #create new webpage entry

        webpg=Webpage.objects.get_or_create(category=top,url=fake_url,name=fake_name)[0]

        #create a fake access record for the Webpage
        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__=='__main__':
    print("populating script!")
    populate()
    print("populating complete!")
