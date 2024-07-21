from apps.shop.models import PickUpModel
from apps.shop.services import PickUpService

from faker import Faker
fake = Faker()

def get_category_params(adres):
    return {
        "adres": adres,
        "description":fake.sentence(),
    }


def perform(*args, **kwargs):
    adres = fake.city()
    # import pdb; pdb.set_trace()
    if not PickUpModel.objects.filter(adres=adres).exists():
        PickUpService.create(get_category_params(adres))
    
