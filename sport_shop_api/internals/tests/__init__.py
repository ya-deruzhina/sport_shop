from internals.tests.product.product_test import ProductViewTestCase
from internals.tests.product.comment_test import CommentViewTestCase
from internals.tests.product.rating_test import RatingViewTestCase
from internals.tests.basket.add_to_basket_from_basket_test import BasketAddFromBasketTestCase
from internals.tests.basket.add_to_basket_from_page_test import BasketAddFromPageTestCase
from internals.tests.basket.delete_from_basket_test import BasketDeleteViewTestCase
from internals.tests.basket.view_basket_test import BasketViewTestCase
from internals.tests.order.order_api_test import OrderCreateTestCase,OrderViewTestCase
from internals.tests.order.one_order_test import OneOrderTestCase
from internals.tests.order.history_of_orders_test import OrdersViewTestCase

all =(
    "ProductViewTestCase",
    "CommentViewTestCase",
    "RatingViewTestCase",
    "BasketAddFromBasketTestCase",
    "BasketAddFromPageTestCase",
    "BasketDeleteViewTestCase",
    "BasketViewTestCase",
    "OrderCreateTestCase",
    "OrderViewTestCase",
    "OneOrderTestCase",
    "OrdersViewTestCase",

)
