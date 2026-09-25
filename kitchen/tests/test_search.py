from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType, Dish, Cook


class SearchTests(TestCase):
    def setUp(self):
        self.user = Cook.objects.create_user(
            username="testuser",
            password="testpassword",
            first_name="Test",
            last_name="User",
            years_of_experience=5
        )
        self.client.force_login(self.user)

    def test_search_dishtype_by_name(self):
        test_dish_type = DishType.objects.create(name="Test Dish Type")
        test_dish_type_2 = DishType.objects.create(name="Test_Dish_Type_2")
        response = self.client.get(
            reverse("kitchen:dish_type_list"),
            {"name": "Test Dish Type"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(test_dish_type, response.context["dish_type_list"])
        self.assertNotIn(test_dish_type_2, response.context["dish_type_list"])

    def test_search_dishtype_is_case_insensitive(self):
        test_dish_type = DishType.objects.create(name="Test Dish Type")
        response = self.client.get(
            reverse("kitchen:dish_type_list"),
            {"name": "test dish type"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(test_dish_type, response.context["dish_type_list"])

    def test_empty_search_returns_all_dish_types(self):
        test_dish_type = DishType.objects.create(name="Test Dish Type")
        response = self.client.get(
            reverse("kitchen:dish_type_list"),
            {"name": ""}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(test_dish_type, response.context["dish_type_list"])

    def test_search_dish_by_name(self):
        dish_type = DishType.objects.create(name="Test Dish Type")
        test_dish = Dish.objects.create(
            name="Test Dish",
            description="Test Description",
            price=10.00,
            dish_type=dish_type,
        )
        response = self.client.get(
            reverse("kitchen:dish_list"),
            {"name": "Test Dish"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(test_dish, response.context["dish_list"])

    def test_search_dish_is_case_insensitive(self):
        dish_type = DishType.objects.create(name="Test Dish Type")
        test_dish = Dish.objects.create(
            name="Test Dish",
            description="Test Description",
            price=10.00,
            dish_type=dish_type,
        )
        response = self.client.get(
            reverse("kitchen:dish_list"),
            {"name": "test dish"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(test_dish, response.context["dish_list"])

    def test_empty_dish_search_returns_all_dishes(self):
        dish_type = DishType.objects.create(name="Test Dish Type")
        test_dish = Dish.objects.create(
            name="Test Dish",
            description="Test Description",
            price=10.00,
            dish_type=dish_type,
        )
        response = self.client.get(
            reverse("kitchen:dish_list"),
            {"name": ""}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(test_dish, response.context["dish_list"])

    def test_search_cook_by_username(self):
        alice = Cook.objects.create_user(
            username="alice_cook",
            password="test_password",
            years_of_experience=5,
        )
        bob = Cook.objects.create_user(
            username="bob_cook",
            password="test_password",
            years_of_experience=5,
        )

        response = self.client.get(
            reverse("kitchen:cook_list"),
            {"username": "alice_cook"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(alice, response.context["cook_list"])
        self.assertNotIn(bob, response.context["cook_list"])

    def test_search_cook_is_case_insensitive(self):
        alice = Cook.objects.create_user(
            username="alice_cook",
            password="test_password",
            years_of_experience=5,
        )
        bob = Cook.objects.create_user(
            username="bob_cook",
            password="test_password",
            years_of_experience=5,
        )

        response = self.client.get(
            reverse("kitchen:cook_list"),
            {"username": "ALICE"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(alice, response.context["cook_list"])
        self.assertNotIn(bob, response.context["cook_list"])

    def test_empty_cook_search_return_all_cooks(self):
        alice = Cook.objects.create_user(
            username="alice_cook",
            password="test_password",
            years_of_experience=5,
        )
        bob = Cook.objects.create_user(
            username="bob_cook",
            password="test_password",
            years_of_experience=5,
        )

        response = self.client.get(
            reverse("kitchen:cook_list"),
            {"username": ""}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(alice, response.context["cook_list"])
        self.assertIn(bob, response.context["cook_list"])
