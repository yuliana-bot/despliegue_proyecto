from django.test import TestCase
from app.models import Cliente


class PruebaBasica(TestCase):
    def test_verificar_entorno(self):
        """Prueba simple para validar que CI/CD funciona"""
        self.assertEqual(1 + 1, 2)

    def test_crear_cliente(self):
        """Prueba básica de base de datos en memoria"""
        # las consultas e inserciones van dentro de las funciones
        Cliente.objects.create(
            nombre='Juan Pérez',
            tipo_documento='CC',
            numero_documento='123456789',
            telefono='3001234567',
        )
        consulta = Cliente.objects.filter(nombre='Juan Pérez')
        self.assertTrue(consulta.exists())