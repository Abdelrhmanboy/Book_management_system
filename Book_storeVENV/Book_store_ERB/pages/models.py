from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name



class Book(models.Model):
    status = [
        ('available', 'available'),
        ('rented', 'rented'),
        ('sold', 'sold'),
    ]

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    book_photo = models.ImageField(upload_to='photos/books', null=True, blank=True)
    author_photo = models.ImageField(upload_to='photos/authors', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    monthly_rental_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rental_period = models.IntegerField(null=True, blank=True)
    rental_total = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=status)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


    def __str__(self):
        return self.title