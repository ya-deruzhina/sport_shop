from django.db import models

class PickUpModel(models.Model):
    adres = models.TextField(null = False)
    description = models.TextField(null = False)
    
    def __str__(self):
        return self.adres