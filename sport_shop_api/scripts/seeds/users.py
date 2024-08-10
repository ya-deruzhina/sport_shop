from apps.users.models import User
from apps.users.services import UsersService
from faker import Faker
fake = Faker()


def get_user_params():
    return {
        "username": "user",
        "email": fake.email(),
        "password": "user",
        "status": User.ACTIVE,
        "is_superuser": False,
        "role": User.USER,
        "is_staff": False,
    }


def perform(*args, **kwargs):
    if not User.objects.filter(username="user").exists():
        UsersService.create(get_user_params())
