from apps.users.views.basket.add_to_basket import BasketAddView
from apps.users.views.basket.basket import BasketView
from apps.users.views.basket.delete_from_basket import BasketDelete
from apps.users.views.order.history_of_orders_api import OrdersUserView
from apps.users.views.order.one_order_api import OneOrdersUserView
from apps.users.views.order.order_api import OrderView
from apps.users.views.products.comment import Comment
from apps.users.views.products.list_of_products import CatalogView
from apps.users.views.products.one_product import ProductView
from apps.users.views.products.rating import Rating


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
)
