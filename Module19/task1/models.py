from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100)  # Username of the buyer
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Account balance
    age = models.PositiveIntegerField()  # Age of the buyer

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)  # Title of the game
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Cost of the game
    size = models.DecimalField(max_digits=10, decimal_places=2)  # File size of the game
    description = models.TextField()  # Game description
    age_limited = models.BooleanField(default=False)  # Age restriction
    buyer = models.ManyToManyField(Buyer, related_name='games')  # Many-to-Many relationship with Buyer

    def __str__(self):
        return self.title
