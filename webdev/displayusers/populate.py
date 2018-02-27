import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'displayusers.settings')

import django
django.setup()

import random
from usersApp.models import User
from faker import Faker

fakegen = Faker()

def populate(N = 10):

    for i in range(N):

        fake_first = fakegen.first_name()
        fake_last = fakegen.last_name()
        fake_email = fakegen.email()

        newuser = User.objects.get_or_create(first = fake_first, last = fake_last, email = fake_email)[0]

if __name__ == '__main__':
    print('Populating...')
    populate()
    print('Population complete!')
