import pytest
from django.test import TestCase
from store.models import *
class DesignerTestCase(TestCase):
    def setUp(self) -> None:
        Designer.objects.create(DesignerId=1,name="mohan",contactnumber='9494949494',designeremailid='mohandeep2002@gmail.com',password='password')
        Designer.objects.create(DesignerId=2, name="Amohan", contactnumber='9490949494',
                                designeremailid='Amohandeep2002@gmail.com', password='password')

    def test_designers2(self):
        ID = Designer.objects.get(DesignerId=1)
        ID = str(ID)
        self.assertEqual(ID, 'Designer object (1)')
    def test_2_desginers2(self):
        ID = Designer.objects.get(DesignerId=2)
        ID = str(ID)
        self.assertEqual(ID, 'Designer object (2)')
