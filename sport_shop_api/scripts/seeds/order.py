from apps.shop.models import OrderModel, GoodsModel,PickUpModel
from apps.users.models import User
from apps.shop.services import OrderService

from faker import Faker
fake = Faker()

import random

TIME_IN_PICK_UP = [
    "9.00-10.00",
    "10.00-11.00",
    "11.00-12.00",
    "12.00-13.00",
    "13.00-14.00",
    "14.00-15.00",
    "15.00-16.00",
    "16.00-17.00",
    "17.00-18.00",
    ]

def get_order_params(user,pick_up_point, date_of_pick_up, time_of_pick_up):
    return {
        "user": user.id,
        "name":user.username,
        "email":user.email,
        "comment":fake.sentence(),
        "pick_up_point":pick_up_point,
        "date_of_pick_up":date_of_pick_up,
        "time_of_pick_up":time_of_pick_up,
        "total_money":random.randint(1, 100),
    }



def perform(*args, **kwargs):
    user = User.objects.all()
    pick_up_point = PickUpModel.objects.all()
    date_of_pick_up = fake.date_this_month() 
    time_of_pick_up = random.choices(TIME_IN_PICK_UP)[0]
    
    for i in user:
        for m in pick_up_point:
            if len(OrderModel.objects.filter(pick_up_point = m.id,date_of_pick_up=date_of_pick_up,time_of_pick_up=time_of_pick_up)) <= 4:
                OrderService.create(get_order_params(i,m.id, date_of_pick_up,time_of_pick_up))