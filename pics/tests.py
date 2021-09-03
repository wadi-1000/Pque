from django.test import TestCase
from .models import Category,Location


# Create your tests here.
class CategoryTestClass(TestCase):

    # Set up method to run tests before
    def setUp(self):
        self.food = Category(category_name = 'Food')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))
    