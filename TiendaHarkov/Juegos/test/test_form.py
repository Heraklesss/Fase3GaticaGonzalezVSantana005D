from django.test import TestCase
from Juegos.forms import VideojuegosForm
from Juegos.models import videojuegos
from django.core.files.uploadedfile import SimpleUploadedFile

class VideojuegoFormsTest(TestCase):
    def test_valid_form(self):
        v = videojuegos.objects.create(name='COD', pegi='18')
        data = {'name': v.name, 'summary': v.pegi,}
        form = VideojuegosForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        v = videojuegos.objects.create(name='', pegi='')
        data = {'name': v.name, 'summary': v.pegi,}
        form = VideojuegosForm(data=data)
        self.assertFalse(form.is_valid())