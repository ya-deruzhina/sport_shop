from django.urls import path,re_path
from apps.shop.views import *
from apps.search.views import * 


urlpatterns = [
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