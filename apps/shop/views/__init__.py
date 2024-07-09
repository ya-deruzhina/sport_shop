from apps.shop.views.basket.add_to_basket import BasketAddView
from apps.shop.views.basket.basket import BasketView
from apps.shop.views.basket.delete_from_basket import BasketDeleteView
from apps.shop.views.order.history_of_orders_api import OrdersUserView
from apps.shop.views.order.one_order_api import OneOrdersUserView
from apps.shop.views.order.order_api import OrderView
from apps.shop.views.products.comment import CommentView
from apps.shop.views.products.catalog import CatalogView
from apps.shop.views.products.one_product import ProductView
from apps.shop.views.products.rating import RatingView
from apps.shop.views.system.page_404 import Page404


all= (
    "BasketAddView",
    "BasketView",
    "BasketDeleteView",
    "OrdersUserView",
    "OneOrdersUserView",
    "OrderView",
    "CommentView",
    "CatalogView",
    "ProductView",
    "RatingView",
    "Page404",
)
