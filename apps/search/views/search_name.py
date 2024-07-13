from apps.search.views import PaginatedElasticSearchAPIView
from apps.shop.serializers import CatalogSerializer
from apps.search.documents import CatalogDocument
from elasticsearch_dsl import Q

class SearchName(PaginatedElasticSearchAPIView):
    serializer_class = CatalogSerializer
    document_class = CatalogDocument

    def generate_q_expression(self, query):
        return Q(
                'multi_match', query=query,
                fields=[
                    'name'
                ], fuzziness='auto')