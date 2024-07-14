from apps.search.views.common_views import PaginatedElasticSearchAPIView
from apps.search.views.search_name import SearchNameView
from apps.search.views.search_category import SearchCategoryView
from apps.search.views.search_description import SearchDescriptionView
from apps.search.views.search_subcategory import SearchSubCategoryView

all= (
    'PaginatedElasticSearchAPIView',
    'SearchNameView', # Полное совпадение
    'SearchCategoryView', # Полное совпадение
    'SearchDescriptionView', # Частичное совпадение
    'SearchSubCategoryView', #Полное совпадение
)

