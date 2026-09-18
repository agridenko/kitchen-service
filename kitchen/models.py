from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.conf import settings


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dish_type_detail', args=[str(self.pk)])


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['years_of_experience']

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name}) - {self.years_of_experience}"

    def get_absolute_url(self):
        return reverse('cook_detail', args=[str(self.pk)])


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name='dishes')

    def __str__(self):
        return self.name
