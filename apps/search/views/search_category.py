from apps.search.views import PaginatedElasticSearchAPIView
from apps.shop.serializers import CatalogSerializer
from apps.shop.models import CategoryModel
from apps.search.documents import CatalogDocument
from elasticsearch_dsl import Q

class SearchCategoryView(PaginatedElasticSearchAPIView):
    serializer_class = CatalogSerializer
    document_class = CatalogDocument

    def generate_q_expression(self, query):
        query = CategoryModel.objects.get(category=query).id
        return Q(
                'multi_match', query=query,
                fields=[
                    'category.id'
                ],)