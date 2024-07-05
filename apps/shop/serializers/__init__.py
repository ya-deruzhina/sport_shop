from apps.shop.serializers.comment.comment_serializer import CommentSerializer
from apps.shop.serializers.rating.rating_serializer import RatingSerializer
from apps.shop.serializers.basket.basket_serializer import BasketSerializer
from apps.shop.serializers.order.order_serializer import OrderSerializer
from apps.shop.serializers.order.product_order_serializer import OrderProductSerializer
from apps.shop.serializers.catalog.catalog import CatalogSerializer


all= (
    'CommentSerializer',
    'RatingSerializer',
    'BasketSerializer',
    'OrderSerializer',
    'OrderProductSerializer',
    'CatalogSerializer',

)

