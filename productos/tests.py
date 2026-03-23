from django.test import TestCase
from django.urls import reverse

from .models import Categoria, Producto


class ProductoViewsTestCase(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre='Electrónica')
        self.producto = Producto.objects.create(
            nombre='Laptop',
            stock=10,
            puntaje=4.5,
            categoria=self.categoria,
        )

    def test_index_view(self):
        response = self.client.get(reverse('productos:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Laptop')

    def test_detalle_view(self):
        response = self.client.get(reverse('productos:detalle', args=[self.producto.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Laptop')

    def test_formulario_get(self):
        response = self.client.get(reverse('productos:formulario'))
        self.assertEqual(response.status_code, 200)

    def test_formulario_post(self):
        response = self.client.post(reverse('productos:formulario'), {
            'nombre': 'Teclado',
            'stock': 5,
            'puntaje': 3.8,
            'categoria': self.categoria.id,
        })
        self.assertRedirects(response, reverse('productos:index'))
        self.assertTrue(Producto.objects.filter(nombre='Teclado').exists())

    def test_editar_get(self):
        response = self.client.get(reverse('productos:editar', args=[self.producto.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Laptop')

    def test_editar_post(self):
        response = self.client.post(reverse('productos:editar', args=[self.producto.id]), {
            'nombre': 'Laptop Pro',
            'stock': 7,
            'puntaje': 4.8,
            'categoria': self.categoria.id,
        })
        self.assertRedirects(response, reverse('productos:detalle', args=[self.producto.id]))
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.nombre, 'Laptop Pro')

    def test_eliminar_get(self):
        response = self.client.get(reverse('productos:eliminar', args=[self.producto.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Laptop')

    def test_eliminar_post(self):
        response = self.client.post(reverse('productos:eliminar', args=[self.producto.id]))
        self.assertRedirects(response, reverse('productos:index'))
        self.assertFalse(Producto.objects.filter(id=self.producto.id).exists())
