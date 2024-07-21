from apps.shop.models import GoodsModel
from apps.users.models import User
from apps.shop.services import CommentService
from faker import Faker
fake = Faker()

author = User.objects.all()[0].id
product = GoodsModel.objects.all()[0].id

def get_comment_params():
    return {
        "author": author,
        "product":product,
        "comment":fake.sentence()
    }



def perform(*args, **kwargs):
    CommentService.create(get_comment_params())
    