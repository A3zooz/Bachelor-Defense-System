from django.db import models

class Constrain(models.Model):
    year =models.IntegerField()
    max_slot_in_day = models.IntegerField()
    min_slot_in_day = models.IntegerField()
    max_num_of_days = models.IntegerField()
    min_num_of_days = models.IntegerField()
    
    def __str__(self) -> str:
        return str(self.year) 