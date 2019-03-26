from django.db import models

# Create your models here.
class task2_funds(models.Model):
    select_funds = models.CharField(max_length=50)

    def _str(self):
        return self.select_funds

    def is_valid(self):
        pass

