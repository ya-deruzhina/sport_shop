from apps.search.views import PaginatedElasticSearchAPIView
from apps.shop.serializers import GoodsSearchSerializer,CatalogSerializer
from apps.shop.models import CategoryModel, SubCategoryModel,ProductsModel
from apps.search.documents import CatalogDocument
from elasticsearch_dsl import Q
from rest_framework.response import Response


class SearchView(PaginatedElasticSearchAPIView):
    serializer_class = GoodsSearchSerializer
    document_class = CatalogDocument

    def generate_q_expression(self,query):
        if query == 'search':
            params = self.request.query_params

            if len(params) == 1:

                if 'category' in params:
                    query = CategoryModel.objects.filter(category=params['category'])
                    if len (query) == 0:
                        query='none'
                        fields='none'
                    else:
                        query = query[0].id
                        fields = [
                            'category.id'
                            ]
                    fuzziness=0

                if 'description' in params:
                    query = params['description']
                    fields=[
                        'description'
                        ]
                    fuzziness='auto'
                    
                if 'name' in params:
                    query = params['name']
                    fields=[
                        'name'
                        ]
                    fuzziness=0
                
                if 'subcategory' in params:
                    query = SubCategoryModel.objects.filter(subcategory=params['subcategory'])
                    if len (query) == 0:
                        query='none'
                        fields='none'
                    else:
                        query = query[0].id
                        fields=[
                            'subcategory.id'
                            ]
                    fuzziness=0


                if fuzziness=='auto':
                    return Q(
                        'multi_match', query=query,
                        fields=fields, fuzziness=fuzziness)
                
                else:
                    return Q(
                        'multi_match', query=query,
                        fields=fields)
            
            else:
                return Q(
                        'multi_match', query='none',
                        fields='none')
            #     keys = params.keys()
            #     all_data = ProductsModel.objects.all()

            #     for key in keys:
            #         if key == 'description':
            #             all_data = all_data.filter(description=params[key])
            #         if key == 'name':
            #             all_data = all_data.filter(name=params[key])
            #         if key == 'category':
            #             all_data = all_data.filter(category=params[key])
            #         if key == 'subcategory':
            #             all_data = all_data.filter(subcategory=params[key])
                
            #     results = []
            #     for data in range(len(all_data)):
            #         results.append(CatalogSerializer(instance=all_data[data]).data)
            #     return Response ({'results':results})

                
