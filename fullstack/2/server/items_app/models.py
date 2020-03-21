from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=100, blank=True, default="")

    class Meta:
        ordering = ["name"]
