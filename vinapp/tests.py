from django.test import TestCase
from vinapp.models import Category

# Create your tests here.
class CategoryMethodTests(TestCase):
    
    def test_ensure_views_are_positive(self):

        cat=Category(name='test',views=-1,likes=0)
        cat.save()
        self.assertEqual((cat.views>=0),True)

    def test_slug_line_creation(self):
         
        cat = cat('Random Category String')
        cat.save()
        self.assertEqual(cat.slug, 'random-category-string')
