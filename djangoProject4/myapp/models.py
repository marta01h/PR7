from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    publication_date = models.DateField()

    def __str__(self):
        return self.title


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.book.price * self.quantity

    def __str__(self):
        return f'{self.book.title} ({self.quantity})'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)

    cart_items = models.ManyToManyField(CartItem, related_name='orders')

    def __str__(self):
        return f'Заказ {self.id} для {self.user.username}'