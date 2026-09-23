from django.test import TestCase
from django.urls import reverse

from kitchen.models import Cook, Dish, DishType


class ModelTest(TestCase):
    def test_dishtype_str(self):
        dish_type = DishType.objects.create(name='Test Dish Type')
        self.assertEqual(str(dish_type), 'Test Dish Type')

    def test_cook_str(self):
        cook = Cook.objects.create_user(
            username='test_cook',
            password='testpassword',
            first_name='Test',
            last_name='Cook',
            years_of_experience=5
        )
        self.assertEqual(
            str(cook),
            f"{cook.username} "
            f"({cook.first_name} {cook.last_name}) - "
            f"{cook.years_of_experience}"
        )

    def test_dish_str(self):
        dish_type = DishType.objects.create(name='Test Dish Type')
        cook = Cook.objects.create_user(
            username='Test Cook',
            password='testpassword',
            years_of_experience=5
        )
        dish = Dish.objects.create(
            name='Test Dish',
            description='Test Dish Description',
            price=10.00,
            dish_type=dish_type
        )
        dish.cooks.set([cook])
        self.assertEqual(str(dish), 'Test Dish')
