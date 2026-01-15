from django.test import TestCase
from LittleLemonAPI.models import MenuItem
from rest_framework.serializers import ModelSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = MenuItem.objects.create(title="Pasta", price=12.50, inventory=50)
        self.item2 = MenuItem.objects.create(title="Pizza", price=15.00, inventory=30)

    def test_menu_items_list(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_single_menu_item_retrieve(self):
        response = self.client.get(f'/restaurant/menu/{self.item1.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], "Pasta")
        self.assertEqual(float(response.data['price']), 12.50)