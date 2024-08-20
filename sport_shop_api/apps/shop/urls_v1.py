from django.urls import path
from apps.shop.views import *
from apps.search.views import * 

from django.urls import path



urlpatterns = [

    # Search
    path('catalog/search_name/<str:query>/', SearchNameView.as_view()),
    path('catalog/search_category/<str:query>/', SearchCategoryView.as_view()),
    path('catalog/search_subcategory/<str:query>/', SearchSubCategoryView.as_view()),
    path('catalog/search_description/<str:query>/',SearchDescriptionView.as_view()),    
    path('catalog/search_by_amount_over/<int:query>/',FilterAmountOverView.as_view()),
    path('catalog/search_by_amount_less/<int:query>/',FilterAmountLessView.as_view()),
    path('catalog/search_by_price/from_min/',FilterPriceMinView.as_view()),
    path('catalog/search_by_price/from_max/',FilterPriceMaxView.as_view()),

    # Product
    path("catalog/",CatalogListView.as_view()),
    path("product/<int:product_id>/",ProductView.as_view()),
    path("product/comment/<int:product_id>/",CommentView.as_view()),
    path("product/rating/<int:product_id>/",RatingView.as_view()),

    # Basket
    path("basket/",BasketView.as_view()),
    path("basket/<int:product_id>/",BasketView.as_view()),
    path("basket/add/<int:basket_id>/",BasketView.as_view()),
    path("basket/delete/<int:basket_id>/",BasketDeleteView.as_view()),

    # Order
    path("orders/",OrdersUserView.as_view()),
    path("order/<int:order_id>/",OneOrdersUserView.as_view()),
    path("order/",OrderView.as_view()),

    # System
    path("404_error/",Page404.as_view()),

]