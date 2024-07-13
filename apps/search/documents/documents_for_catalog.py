# from django.contrib.auth.models import User
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from apps.shop.models import GoodsModel, CategoryModel, SubCategoryModel


@registry.register_document
class CatalogDocument(Document):
    category = fields.ObjectField(properties={
        # 'id': fields.IntegerField(),
        'category' : fields.TextField()
    })
    subcategory = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        # 'subcategory' : fields.TextField(),
        # 'category' : fields.TextField()
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
            'price',
        ]
        related_models = [CategoryModel, SubCategoryModel]


# from django.conf import settings
# from django_elasticsearch_dsl import Document, Index, fields
# from elasticsearch_dsl import analyzer

# from apps.shop.models import GoodsModel
# from settings.common import ELASTICSEARCH_INDEX_NAMES

# # Name of the Elasticsearch index
# INDEX = Index(ELASTICSEARCH_INDEX_NAMES[__name__])

# # See Elasticsearch Indices API reference for available settings
# INDEX.settings(
#     number_of_shards=1,
#     number_of_replicas=1
# )
# html_strip = analyzer(
#     'html_strip',
#     tokenizer="standard",
#     filter=["standard", "lowercase", "stop", "snowball"],
#     char_filter=["html_strip"]
# )
# @INDEX.doc_type
# class CatalogDocument(Document):
#     """Book Elasticsearch document."""

#     id = fields.IntegerField(attr='id')

#     name = fields.StringField(
#         analyzer=html_strip,
#         fields={
#             'raw': fields.StringField(analyzer='keyword'),
#         }
#     )

#     price = fields.FloatField()


#     class Django(object):
#         """Inner nested class Django."""

#         model = GoodsModel  # The model associate with this Document

