from apps.shop.views.basket.basket import BasketView
from apps.shop.views.basket.delete_from_basket import BasketDeleteView
from apps.shop.views.order.history_of_orders_api import OrdersUserView
from apps.shop.views.order.one_order_api import OneOrdersUserView
from apps.shop.views.order.order_api import OrderView
from apps.shop.views.products.comment import CommentView
from apps.shop.views.products.catalog import CatalogListView
from apps.shop.views.products.one_product import ProductView
from apps.shop.views.products.rating import RatingView
from apps.shop.views.system.page_404 import Page404
from apps.shop.views.filters.filter_by_price_max import FilterPriceMaxView
from apps.shop.views.filters.filter_by_price_min import FilterPriceMinView
from apps.shop.views.filters.filter_amount_less import FilterAmountLessView
from apps.shop.views.filters.filter_amount_over import FilterAmountOverView


all= (
    "BasketView",
    "BasketDeleteView",
    "OrdersUserView",
    "OneOrdersUserView",
    "OrderView",
    "CommentView",
    "ProductView",
    "RatingView",
    "Page404",
    "FilterPriceMinView",
    "FilterPriceMaxView",
    "FilterAmountOverView",
    "FilterAmountLessView",
    "CatalogListView"
)
