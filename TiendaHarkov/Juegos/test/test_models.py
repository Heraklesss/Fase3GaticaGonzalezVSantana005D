from django.test import TestCase
from Juegos.models import videojuegos

#Create your tests here.

class GameTestCase(TestCase):

    @classmethod

    def setUpTestData(cls):
        test_juego = videojuegos.objects.create(name='COD',pegi='p18')

    def test_name_label(self):
        juego=videojuegos.objects.get(id=1)
        field_label = videojuegos._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_pegi_label(self):
        juego=videojuegos.objects.get(id=1)
        field_label = videojuegos._meta.get_field('pegi').verbose_name
        self.assertEquals(field_label,'pegi')

    def test_name_max_length(self):
        juego=videojuegos.objects.get(id=1)
        max_length = videojuegos._meta.get_field('name').max_length
        self.assertEquals(max_length,200)

    def test_pegi_max_length(self):
        juego=videojuegos.objects.get(id=1)
        max_length = videojuegos._meta.get_field('pegi').max_length
        self.assertEquals(max_length,3)

    def test_get_absolute_url(self):
        juego=videojuegos.objects.get(id=1)
        self.assertEquals(game.get_absolute_url(), '/Juegos/game/1')