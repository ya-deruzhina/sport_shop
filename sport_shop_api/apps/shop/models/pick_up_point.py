from django.db import models

class PickUpModel(models.Model):
    address = models.CharField(max_length = 50, null = False)
    description = models.TextField(null = False)
    
    def serilize_from_db (self):
        return (self.address)