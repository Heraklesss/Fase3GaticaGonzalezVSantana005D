from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from Juegos.models import videojuegos

class JuegosListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_juegos = 13

        for videojuegos in range(number_of_juegos):
            videojuegos.objects.create(
                name=f'COD {videojuegos}',
                pegi=f'18 {videojuegos}',
            )
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/Juegos/videojuegos/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('videojuegos'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('videojuegos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Juegos/videojuegos_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('videojuegos'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['videojuegos_list']) == 10)

    def test_lists_all_genres(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('videojuegos')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['videojuegos_list']) == 3)
        
   
    