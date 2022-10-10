import factory
import faker
from . import models

faker = faker.Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.MyUser
    
    first_name = faker.first_name()
    last_name = faker.last_name()
    email = factory.Sequence(lambda n: faker.email())
    phone = '078 XXX XXXX'
    date_of_birth = str(faker.date_of_birth())
    password = f'{faker.phone_number()}{faker.last_name()}{faker.phone_number()}'