from apps.shop.models import ProductsModel, CommentOfProductsModel
from apps.users.models import User
from apps.shop.services import CommentService
from faker import Faker
fake = Faker()

def get_comment_params(author, product):
    return {
        "author": author,
        "product":product,
        "comment":fake.sentence()
    }



def perform(*args, **kwargs):
    goods = ProductsModel.objects.all()
    author = User.objects.all()
    if len(CommentOfProductsModel.objects.all()) == 0:
        for i in goods:
            for m in author:
                if not CommentOfProductsModel.objects.filter(product = i.id, author = m.id).exists():
                    CommentService.create(get_comment_params(m.id, i.id))
        