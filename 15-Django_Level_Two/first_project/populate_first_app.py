# Os imports devem seguir a ordem em que foram definidos e devido ao autosort de imports
# do plugin do vscode os imports estavam sendo inseridos de forma errada. Para corrigir
# esse problema foi adicionada uma configuração no arquivo .vscode/settings.json para
# desativar a regra pep "E402: module level import not at top of file".
# "python.formatting.autopep8Args": ["--ignore", "E402"]

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')


import django
django.setup()


import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker


# FAKE POP SCRIPT

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):

        # get the topic for the entry
        top = add_topic()

        # Create the fake data for the entry
        fake_url = fakegen.url()
        fake_data = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(
            topic=top, url=fake_url, name=fake_name)[0]

        # Create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(
            name=webpg, date=fake_data)[0]


if __name__ == '__main__':
    print("Populating Script!")
    populate(20)
    print("Populating Complete!")
