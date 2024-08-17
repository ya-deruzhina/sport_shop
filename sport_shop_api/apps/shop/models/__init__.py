from apps.shop.models.basket import BasketModel
from apps.shop.models.comment import CommentOfProductsModel
from apps.shop.models.products import ProductsModel
from apps.shop.models.order import OrderModel
from apps.shop.models.pick_up_point import PickUpModel
from apps.shop.models.product_in_order import ProductInOrder
from apps.shop.models.rating import RatingOfProductsModel
from apps.shop.models.category import CategoryModel
from apps.shop.models.subcategory import SubCategoryModel


all= (
    'BasketModel',
    'CommentOfProductsModel',
    'ProductsModel',
    'OrderModel',
    'PickUpModel',
    'ProductInOrder',
    'RatingOfProductsModel',
    'CategoryModel', 
    'SubCategoryModel',
)

