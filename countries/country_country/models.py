from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=20)
    local_currency = models.CharField(max_length=20)
    added_on = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.country_name
