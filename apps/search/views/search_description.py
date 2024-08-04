from apps.search.views import PaginatedElasticSearchAPIView
from apps.shop.serializers import GoodsSearchSerializer
from apps.search.documents import CatalogDocument
from elasticsearch_dsl import Q

class SearchDescriptionView(PaginatedElasticSearchAPIView):
    serializer_class = GoodsSearchSerializer
    document_class = CatalogDocument

    def generate_q_expression(self, query):
        return Q(
                'multi_match', query=query,
                fields=[
                    'description'
                ], fuzziness='auto')