from django.db import models
from apps.users.models.pick_up_point import PickUpModel


class TimePickUpModel(models.Model):    
    AM_9_10 = "9.00-10.00"
    AM_10_11 = "10.00-11.00"
    AM_11_12 = "11.00-12.00"
    PM_12_1 = "12.00-13.00"
    PM_1_2 = "13.00-14.00"
    PM_2_3 = "14.00-15.00"
    PM_3_4 = "15.00-16.00"
    PM_4_5 = "16.00-17.00"
    PM_5_6 ="17.00-18.00"

    TIME_IN_PICK_UP = [
    (AM_9_10, "9.00-10.00"),
    (AM_10_11, "10.00-11.00"),
    (AM_11_12, "11.00-12.00"),
    (PM_12_1, "12.00-13.00"),
    (PM_1_2, "13.00-14.00"),
    (PM_2_3, "14.00-15.00"),
    (PM_3_4,"15.00-16.00"),
    (PM_4_5,"16.00-17.00"),
    (PM_5_6,"17.00-18.00"),
    ]

    pick_up_point = models.ForeignKey(PickUpModel, null=False, on_delete=models.CASCADE)
    date_of_pick_up = models.DateField()
    time_of_pick_up = models.CharField (choices=TIME_IN_PICK_UP,max_length = 100)
    count = models.IntegerField (default=5)