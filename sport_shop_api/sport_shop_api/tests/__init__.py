from sport_shop_api.tests.product.product_test import ProductViewTestCase
from sport_shop_api.tests.product.comment_test import CommentViewTestCase
from sport_shop_api.tests.product.rating_test import RatingViewTestCase
from sport_shop_api.tests.basket.add_to_basket_from_basket_test import BasketAddFromBasketTestCase
from sport_shop_api.tests.basket.add_to_basket_from_page_test import BasketAddFromPageTestCase
from sport_shop_api.tests.basket.delete_from_basket_test import BasketDeleteViewTestCase
from sport_shop_api.tests.basket.view_basket_test import BasketViewTestCase
from sport_shop_api.tests.order.order_api_test import OrderCreateTestCase,OrderViewTestCase
from sport_shop_api.tests.order.one_order_test import OneOrderTestCase
from sport_shop_api.tests.order.history_of_orders_test import OrdersViewTestCase

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
