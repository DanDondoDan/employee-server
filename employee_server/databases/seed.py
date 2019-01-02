import os
import django

django.setup()

from django_seed import Seed
from employee_server import models
import random
from faker import Faker

# CHOICE = ["sales manager", "project manager"]
CHOICE1 = ["sales department", "director"]
CHOICE = ["sales department"]
seeder = Seed.seeder()

# seeder.add_entity(models.User, 50000)
# seeder.add_entity(models.Position, 50000)
# seeder.add_entity(models.Person, 50000)
# seeder.add_entity(models.Position, 50000)
# inserted_pks = seeder.execute()

"""
seeder.add_entity(models.Position, 100, {
    'position': lambda x: random.choice(CHOICE),
    
})
"""
seeder.add_entity(models.Unit, 10, {
    'id': lambda x: random.randint(0,1000),
    'name': CHOICE,
    'parent': lambda x: random.choice(CHOICE1),
    'plural_name': CHOICE,
    
    
})

# seeder.execute()
inserted_pks = seeder.execute()
print(inserted_pks)
