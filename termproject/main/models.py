from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=30)
    weight = models.FloatField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name="items")
    stocked_date = models.DateField()


class ItemStoredHistory(models.Model):
    weight = models.FloatField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="histories")
    op_code = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)