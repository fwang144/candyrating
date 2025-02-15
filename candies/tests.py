from django.test import TestCase

# Create your tests here.
from candies.models import Candy


class CandyTestCase(TestCase):

    def setUp(self):
        Candy.objects.create(name = "Dubai Chocolate", type = "Nutty Chocolate", rating = 9)
        Candy.objects.create(name = "Truffle", type ="chocolate bit", rating = 7)

    def test_detail_model(self):
        # Get the object
        dubaiChocolate = Candy.objects.get(name = "Dubai Chocolate")
        truffle = Candy.objects.get(name = "Truffle")

        # Assert that the object is matched
        self.assertEqual(dubaiChocolate.type, "Nutty Chocolate")
        self.assertEqual(truffle.type, "chocolate bit")

    def test_update_model(self):
        # Get the Candy Model
        dubaiChocolate = Candy.objects.get(name = "Dubai Chocolate")
        dubaiChocolate.name = "Dubai Chocolate version 2"

        #Change the name of the Candy Model
        truffle = Candy.objects.get(name = "Truffle")
        truffle.name = "Cherry Truffle"

        # Assert that the object is updated match
        self.assertEqual(dubaiChocolate.name, "Dubai Chocolate version 2")
        self.assertEqual(truffle.name, "Cherry Truffle")

    def test_delete_model(self):
        # Get the object
        obj = Candy.objects.get(name="Dubai Chocolate")
        
        # Delete the object
        obj.delete()

        # Attempt to retrieve the deleted object
        deleted_obj = Candy.objects.filter(id=obj.id).first()

        # Assert that the object is deleted
        self.assertIsNone(deleted_obj)