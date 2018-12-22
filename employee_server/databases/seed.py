import os
import django
django.setup()

from django_seed import Seed
from employee_server import models




seeder = Seed.seeder()

seeder.add_entity(models.User, 1)


inserted_pks = seeder.execute()
"""
seeder.add_entity(Player, 10, {
    'score':    lambda x: random.randint(0,1000),
    'nickname': lambda x: seeder.faker.email(),
})
seeder.execute()
"""