from apps.search.views import PaginatedElasticSearchAPIView
from apps.shop.serializers import GoodsSearchSerializer
from apps.shop.models import SubCategoryModel
from apps.search.documents import CatalogDocument
from elasticsearch_dsl import Q

class SearchSubCategoryView(PaginatedElasticSearchAPIView):
    serializer_class = GoodsSearchSerializer
    document_class = CatalogDocument

    def generate_q_expression(self, query):
        query = SubCategoryModel.objects.get(subcategory=query).id
        return Q(
                'multi_match', query=query,
                fields=[
                    'subcategory.id'
                ])