from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from apps.shop.models import GoodsModel


@registry.register_document
class CatalogDocument(Document):
    category = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'category' : fields.TextField()
    })
    subcategory = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'subcategory' : fields.TextField(),
        'id_parent' : fields.Completion({
            'id': fields.IntegerField(),
            'category' : fields.TextField()
        })
    })

    class Index:
        {
            "index.blocks.read_only_allow_delete": None,
            "index.blocks.read_only": False
        }
        name = 'search'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = GoodsModel
        fields = [
            'name',
            'description',
            'price',
            'amount',
            
        ]