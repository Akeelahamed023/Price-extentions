from django.db import models


class CategoryChoices(models.Model):
    CategoryChoices = models.CharField(max_length=100)
    def __str__(self):
        return self.CategoryChoices
    
class BrandChoices(models.Model):
    BrandChoices = models.CharField(max_length=100)
    def __str__(self):
        return self.BrandChoices
    
class ModelChoices(models.Model):
    ModelChoices = models.CharField(max_length=100)
    def __str__(self):
        return self.ModelChoices
    

# Create your models here.
class PhoneData(models.Model):
    Category = models.ForeignKey(CategoryChoices, on_delete=models.CASCADE)
    brand = models.ForeignKey(BrandChoices, on_delete=models.CASCADE)
    model = models.ForeignKey(ModelChoices, on_delete=models.CASCADE)
    price = models.FloatField()
    link = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.Category} - {self.brand} - {self.model}"
    
