from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):

    status_book = [
        ('available','available'),
        ('rental','rental'),
        ('sold','sold'),
    ]

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, blank=True, null=True)
    photo_book = models.ImageField(upload_to='photo_book', blank=True, null=True)
    photo_author = models.ImageField(upload_to='photo_author', blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    retal_price_day = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    retal_period = models.IntegerField(blank=True, null=True)
    total_rental = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=status_book, blank=True, null=True) 
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)


    def __str__(self):
        return self.title