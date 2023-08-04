from django.db import models


# Create your models here.
class CategoryModel(models.Model):
    categoryId = models.IntegerField(primary_key=True)
    categoryName = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.categoryName