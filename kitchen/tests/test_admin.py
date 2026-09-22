from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password='testpass123'
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="some_cook",
            password='testpass123',
            first_name='Test',
            last_name='User',
            years_of_experience=5
        )

    def test_cook_years_of_experience(self):
        """Test that the years of experience
        field is displayed on the admin page"""
        url = reverse('admin:kitchen_cook_changelist')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.cook.years_of_experience)
