from django.urls import path
from apps.shop.views import * 

urlpatterns = [

    # Catalog
    path("catalog/",CatalogView.as_view()),

    # Product
    path("product/<int:product_id>/",ProductView.as_view()),
    path("product/comment/",Comment.as_view()),
    path("product/rating/",Rating.as_view()),

    # Basket
    path("basket/",BasketView.as_view()),
    path("basket/add/",BasketAddView.as_view()),
    path("basket/delete/",BasketDelete.as_view()),

    # Order
    path("user/orders/",OrdersUserView.as_view()),
    path("user/order/",OneOrdersUserView.as_view()),
    path("order/",OrderView.as_view()),

]