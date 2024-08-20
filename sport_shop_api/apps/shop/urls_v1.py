from django.urls import path,re_path
from apps.shop.views import *
from apps.search.views import * 




urlpatterns = [

    # Search
    # Search by price and amount work in path catalog/?
    #         max_price = 10
    #         min_price = 10
    #         price_from_min
    #         price_from_max

    #         max_amount = 10
    #         min_amount = 10
    #         amount_from_min
    #         amount_from_max

    # Search by params work in path catalog/<str:query>/? query==search
    #         a complete match
    #         category
    #         name
    #         subcategory
            
    #         partial match
    #         description 
    path('catalog/<str:query>/', SearchView.as_view()),
    path("catalog/",CatalogListView.as_view()),

    # Product
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