from apps.shop.models import PickUpModel
from apps.shop.services import PickUpService

from faker import Faker
fake = Faker()

adres = "Mogilev"

def get_category_params():
    return {
        "adres": adres,
        "description":fake.sentence(),
    }


def perform(*args, **kwargs):
    if not PickUpModel.objects.filter(adres=adres).exists():
        PickUpService.create(get_category_params())
    
