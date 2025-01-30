from django.test import TestCase

# Create your tests here.
from candies.models import Candy


class CandyTestCase(TestCase):

    def setUp(self):
        Candy.objects.create(name = "Dubai Chocolate", type = "Nutty Chocolate", rating = 9)
        Candy.objects.create(name = "Truffle", type ="chocolate bit", rating = 7)

    def test_detail_model(self):
        dubaiChocolate = Candy.objects.get(name = "Dubai Chocolate")
        truffle = Candy.objects.get(name = "Truffle")
        self.assertEqual(dubaiChocolate.type, "Nutty Chocolate")
        self.assertEqual(truffle.type, "chocolate bit")