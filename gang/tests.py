from django.test import TestCase
from .models import Neighbourhood
# Create your tests here.
class HoodTestClass(TestCase):
    def setUp(self):
        self.hood = Neighbourhood(hood_name="kibra", hood_location="nairobi")
        # self.gang = Neighbourhood(hood_name="kayole", hood_location="mtaa")
        

    def tearDown(self):
        Neighbourhood.objects.all().delete()

    def test_creation_of_hood_test(self):
        self.hood.save()
        self.gang = Neighbourhood.create_neighbourhood("makish", "nest")
        self.assertTrue(isinstance(self.gang, Neighbourhood))
        #self.assertEqual(len(Neighbourhood.objects.all()), 2)

    def test_neighbourhood_delete(self):
        self.hood.save()
        self.gang = Neighbourhood.create_neighbourhood("hello","world")
        self.hood.delete_neighbourhood()
        self.assertEqual(len(Neighbourhood.objects.all()), 1)

    def test_search_by_id(self):
        self.hood.save()
        self.gang = Neighbourhood.create_neighbourhood("hello", "world")
        # print(Neighbourhood.objects.all())
        # print(self.hood.id)
        # print(self.gang.id)
        found_hood = Neighbourhood.objects.get(id=self.hood.id)
        search_hood = Neighbourhood.find_neigborhood(self.hood.id)
        self.assertEqual(found_hood, search_hood)
