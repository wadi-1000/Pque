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

      # Testing Save Method
    def test_save_method(self):
        self.food.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)


class LocationTestClass(TestCase):

    # Set up method to run tests before
    def setUp(self):
        self.Nairobi = Category(category_name = 'Nairobi')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Nairobi,Loaction))

      # Testing Save Method
    def test_save_method(self):
        self.Nairobi.save_category()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)  


    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()



class ImageTestClass(TestCase):
    def setUp(self):
        self.globe = Image(name = 'globe', description = 'a globe pic')
        self.globe.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.globe, Image))

    def test_save_method(self):
        self.globe.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)            

    def test_delete_method(self):
        self.new_image = Image(name = 'intercontinental', description = 'a birds eye view of the Intercontinental hotel')  
        self.new_image.save_image() 
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertEqual(len(images), 1)

    def test_update_method(self):
        self.car = Image(name = 'car', description = 'a blue car')
        self.car.save_image()
        self.car = Image(name = 'car', description = 'a blue car')        
        self.car.update_image(name = 'car')
        self.car.save_image()
        images = Image.objects.filter(name = 'car')
        pics = Image.objects.all()       
        self.assertEqual(len(images), 1)
