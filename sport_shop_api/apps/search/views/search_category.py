from apps.search.views import PaginatedElasticSearchAPIView
from apps.shop.serializers import GoodsSearchSerializer
from apps.shop.models import CategoryModel
from apps.search.documents import CatalogDocument
from elasticsearch_dsl import Q

class SearchCategoryView(PaginatedElasticSearchAPIView):
    serializer_class = GoodsSearchSerializer
    document_class = CatalogDocument

    def generate_q_expression(self, query):
        query = CategoryModel.objects.filter(category=query)[0].id
        return Q(
                'multi_match', query=query,
                fields=[
                    'category.id'
                ],)