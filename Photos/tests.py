from django.test import TestCase
from .models import Location, gallery, Category

# Create your tests here.

class GalleryTestClass(TestCase):
    def SetUp(self):
        self.new_imageLocation = gallery.imageLocation(
            imageLocation_name='Taita')
        self.new_imageLocation.save()

        self.new_imageCategory = gallery.imageCategory(
            imageCategory_name='Business')
        self.new_imageCategory.save()

        self.new_pic = gallery(image='image.jpeg', imageName='screenshot', imageDescription='Just a way in and out',
                               imageLocation=self.new_imageLocation, imageCategory=self.new_imageCategory)
        self.new_pic.save()

    def tearDown(self):
        gallery.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pic, gallery))

    def test_save_new(self):
        self.new_pic.save_gallery()
        galleria = gallery.objects.all()
