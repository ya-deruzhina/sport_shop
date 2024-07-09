from django.db import models

class PickUpModel(models.Model):
    adres = models.CharField(max_length = 50, null = False)
    description = models.TextField(null = False)
    
    def __str__(self):
        return self.adres