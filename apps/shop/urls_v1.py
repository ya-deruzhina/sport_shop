from django.urls import path
from apps.shop.views import * 

urlpatterns = [

    # Catalog
    path("catalog/",CatalogView.as_view()),

    # Product
    path("product/<int:product_id>/",ProductView.as_view()),
    path("product/comment/<int:product_id>/",CommentView.as_view()),
    path("product/rating/<int:product_id>/",RatingView.as_view()),

    # Basket
    path("basket/",BasketView.as_view()),
    path("basket/add/",BasketAddView.as_view()),
    path("basket/delete/",BasketDeleteView.as_view()),

    # Order
    path("user/orders/",OrdersUserView.as_view()),
    path("user/order/",OneOrdersUserView.as_view()),
    path("order/",OrderView.as_view()),

    # System
    path("404_error/",Page404.as_view()),

]