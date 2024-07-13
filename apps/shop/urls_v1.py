from django.urls import path
from apps.shop.views import *
from apps.search.views import * 

from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
# router.register(r"search", CatalogSearchViewSet)
# router.register(r"search", SearchName.as_view())


urlpatterns = [

    # Catalog
    # path("catalog/",CatalogView.as_view()),
    path("catalog/",include(router.urls)),
    # path('', include(router.urls)),
    path('catalog/<str:query>/', SearchName.as_view()),

    # Product
    path("product/<int:product_id>/",ProductView.as_view()),
    path("product/comment/<int:product_id>/",CommentView.as_view()),
    path("product/rating/<int:product_id>/",RatingView.as_view()),

    # Basket
    path("basket/",BasketView.as_view()),
    path("basket/<int:product_id>/",BasketView.as_view()),
    path("basket/add/<int:basket_id>/",BasketAddView.as_view()),
    path("basket/delete/<int:basket_id>/",BasketDeleteView.as_view()),

    # Order
    path("orders/",OrdersUserView.as_view()),
    path("order/<int:order_id>/",OneOrdersUserView.as_view()),
    path("order/",OrderView.as_view()),

    # System
    path("404_error/",Page404.as_view()),

]