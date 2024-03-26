from event_platform.accounts.models import User
from django.core.management.base import BaseCommand
from faker import Faker

fake = Faker()

def create_users(num_of_user):
    users = []
    for _ in range(num_of_user):
        username = fake.user_name()
        first_name = fake.first_name(),
        last_name = fake.last_name(),
        email = fake.email(),
        url_image = fake.image_url()
        user = User.objects.create_user(username = username, firstname = first_name, lastname = last_name, email = email, urlimage = url_image)
        users.append(user)
    return users


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = create_users(10)

