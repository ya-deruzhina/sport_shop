from apps.shop.models import PickUpModel
from apps.shop.services import PickUpService

from faker import Faker
fake = Faker()

def get_point_params():
    return {
        "address": fake.city(),
        "description":fake.sentence(),
    }


def perform(*args, **kwargs):
    if len(PickUpModel.objects.all()) == 0:
        PickUpService.create(get_point_params())
