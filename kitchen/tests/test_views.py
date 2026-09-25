from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType, Dish, Cook


class PublicViewsTests(TestCase):
    def test_login_required_for_index_page(self):
        response = self.client.get(reverse("kitchen:index"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_for_dish_list_page(self):
        response = self.client.get(reverse("kitchen:dish_list"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_for_dish_detail_page(self):
        dish_type = DishType.objects.create(name="Test Dish Type")
        cook = Cook.objects.create_user(
            username="Test Cook",
            password="testpassword",
            years_of_experience=5
        )
        dish = Dish.objects.create(
            name="Test Dish",
            description="Test Description",
            price=10.00,
            dish_type=dish_type,
        )
        dish.cooks.set([cook])
        url = reverse("kitchen:dish_update", kwargs={"pk": dish.pk})
        response = self.client.get(url)
        self.assertRedirects(response, f"/accounts/login/?next={url}")

    def test_login_required_for_dish_type_list_page(self):
        response = self.client.get(reverse("kitchen:dish_type_list"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_for_cook_list_page(self):
        response = self.client.get(reverse("kitchen:cook_list"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_for_cook_detail_page(self):
        cook = Cook.objects.create_user(
            username="Test Cook",
            password="testpassword",
            first_name="Test",
            last_name="Cook",
            years_of_experience=5
        )
        url = reverse("kitchen:cook_detail", kwargs={"pk": cook.pk})
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)


class PrivateViewsTests(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create_user(
            username="Test Cook",
            password="testpassword",
            first_name="Test",
            last_name="Cook",
            years_of_experience=5
        )
        self.client.force_login(self.cook)

    def test_index_page_displays_correct_context(self):
        dish_type = DishType.objects.create(name="Test Dish Type")
        Dish.objects.create(
            name="Test Dish",
            dish_type=dish_type,
            price=10.00,
        )
        Cook.objects.create_user(
            username="test_cook",
            password="testpassword",
            first_name="Test",
            last_name="Cook",
            years_of_experience=5
        )

        response = self.client.get(reverse("kitchen:index"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["num_dish_types"], 1)
        self.assertEqual(response.context["num_dishes"], 1)
        self.assertEqual(response.context["num_cooks"], 2)

    def test_dish_type_list_page_uses_correct_display(self):
        response = self.client.get(reverse("kitchen:dish_type_list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dishtype_list.html")

    def test_cook_list_page_uses_correct_display(self):
        response = self.client.get(reverse("kitchen:cook_list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/cook_list.html")

    def test_dish_list_page_uses_correct_display(self):
        response = self.client.get(reverse("kitchen:dish_list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_list.html")
