# from django.contrib.auth.models import User
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from apps.shop.models import GoodsModel, CategoryModel, SubCategoryModel


@registry.register_document
class CatalogDocument(Document):
    category = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'category' : fields.TextField()
    })
    subcategory = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'subcategory' : fields.TextField(),
        'category' : fields.TextField()
    })

    class Index:
        name = 'search'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = GoodsModel
        fields = [
            'name',
            'description',
            'price',
            'amount',
            
        ]
        related_models = [CategoryModel, SubCategoryModel]