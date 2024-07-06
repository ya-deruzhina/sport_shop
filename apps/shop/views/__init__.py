from apps.shop.views.basket.add_to_basket import BasketAddView
from apps.shop.views.basket.basket import BasketView
from apps.shop.views.basket.delete_from_basket import BasketDelete
from apps.shop.views.order.history_of_orders_api import OrdersUserView
from apps.shop.views.order.one_order_api import OneOrdersUserView
from apps.shop.views.order.order_api import OrderView
from apps.shop.views.products.comment import Comment
from apps.shop.views.products.list_of_products import CatalogView
from apps.shop.views.products.one_product import ProductView
from apps.shop.views.products.rating import Rating
from apps.shop.views.system.page_404 import Page404


all= (
    "BasketAddView",
    "BasketView",
    "BasketDelete",
    "OrdersUserView",
    "OneOrdersUserView",
    "OrderView",
    "Comment",
    "CatalogView",
    "ProductView",
    "Rating",
    "Page404",
)
