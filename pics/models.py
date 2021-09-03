from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def search_by_title(cls,search_term):
        items = cls.objects.filter(title__icontains=search_term)
        return items
  

class Location(models.Model):
    name = models.CharField(max_length = 30)  

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()



class Image(models.Model):
    photo = CloudinaryField('photo')
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 80)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,id,image):
        cls.objects.filter(id=id).update(photo=image)

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def search_image(cls,category):
        try:
            searched = Category.objects.get(name = category)
            images = Image.objects.filter(category = searched.id)
            return images
        except Exception:
            return  "No images were found for that category"

    @classmethod
    def filter_by_location(cls,location):
        searched = Location.objects.get(name = location)
        images = Image.objects.filter(location = searched.id)
        return images 

    @classmethod
    def display_all_images(cls):
        return cls.objects.all()

    class Meta:
        ordering = ['-post_date']   