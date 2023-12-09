from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='카테고리명')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '카테고리'
        verbose_name_plural = '카테고리'


class Item(models.Model):
    name = models.CharField(max_length=30, verbose_name='상품명')
    weight = models.FloatField(verbose_name='현재 재고')
    minimum_weight = models.FloatField(verbose_name='최소 유지 재고')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name="items",
                                 verbose_name='카테고리')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '상품'
        verbose_name_plural = '상품'


class ItemStoredHistory(models.Model):
    op_code = [
        ('출고', False),
        ('입고', True),
    ]

    weight = models.FloatField(verbose_name='입/출고량')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="histories")
    op_code = models.BooleanField(choices=op_code, verbose_name='입고/출고')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '입출고 기록'
        verbose_name_plural = '입출고 기록'
