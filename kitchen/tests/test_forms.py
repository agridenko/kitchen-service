from django.test import TestCase

from kitchen.forms import DishTypeForm, DishForm, CookCreationForm
from kitchen.models import DishType, Cook


class DishTypeFormTest(TestCase):
    """Test the DishTypeForm"""

    def test_dish_type_form(self):
        """Test that the dish type form is valid"""
        form_data = {
            "name": "Test Dish Type"
        }
        form = DishTypeForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_type_form_invalid(self):
        """Test that the dish type form is invalid"""
        form_data = {
            "name": ""
        }
        form = DishTypeForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)


class DishFormTest(TestCase):
    """Test the DishForm"""

    def setUp(self):
        self.dish_type = DishType.objects.create(name="Test Dish Type")
        self.cook = Cook.objects.create_user(
            username="Test Cook",
            password="testpass123",
            first_name="Test",
            last_name="Cook",
            years_of_experience=5
        )

    def test_dish_form(self):
        """Test that the dish form is valid"""
        form_data = {
            "name": "Test Dish",
            "description": "Test Dish Description",
            "price": 10.00,
            "dish_type": self.dish_type.pk,
            "cooks": [self.cook.pk]
        }
        form = DishForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_dish_form_invalid(self):
        """Test that the dish form is invalid"""
        form_data = {
            "name": "",
            "description": "Test Dish Description",
            "price": 10.00,
            "dish_type": self.dish_type.pk,
            "cooks": [self.cook.pk]
        }

        form = DishForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)


class CookFormTest(TestCase):
    """Test the CookForm"""

    def test_cook_form(self):
        """Test that the cook form is valid"""
        form_data = {
            "username": "test_cook",
            "password1": "testpass123",
            "password2": "testpass123",
            "first_name": "Test",
            "last_name": "Cook",
            "years_of_experience": 5
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cook_form_invalid(self):
        """Test that the cook form is invalid"""
        form_data = {
            "username": "",
            "password1": "testpass123",
            "password2": "testpass123",
            "first_name": "Test",
            "last_name": "Cook",
            "years_of_experience": 5
        }
        form = CookCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)
