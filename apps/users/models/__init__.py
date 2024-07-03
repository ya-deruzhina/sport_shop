from apps.users.models.basket import BasketModel
from apps.users.models.comment import CommentOfGoodsModel
from apps.users.models.goods import GoodsModel
from apps.users.models.order import OrderModel
from apps.users.models.pick_up_point import PickUpModel
from apps.users.models.product_in_order import ProductInOrder
from apps.users.models.rating import RatingOfGoodsModel
from apps.users.models.teg import TegsOfGoodsModel
from apps.users.models.time_pick_up import TimePickUpModel
from apps.users.models.user import User


all= (
    'BasketModel',
    'CommentOfGoodsModel',
    'GoodsModel',
    'OrderModel',
    'PickUpModel',
    'ProductInOrder',
    'RatingOfGoodsModel',
    'TegsOfGoodsModel',
    'TimePickUpModel',
    'User'
)

