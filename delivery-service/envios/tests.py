from rest_framework.test import APITestCase
from rest_framework import status
from .models import Envio


class EnvioCRUDTestCase(APITestCase):

    def setUp(self):
        self.envio_base = Envio.objects.create(
            numero_guia="GUIA-TEST-001",
            id_usuario=1,
            id_empresa=1,
            direccion_origen="Calle 1 # 2-3",
            direccion_destino="Carrera 4 # 5-6",
            destinatario_nombre="Juan Pérez",
            destinatario_telefono="3001234567",
            estado="pendiente",
            costo_envio=15000.00,
            activo=1
        )
        self.url_list = "/api/envios/"
        self.url_detail = f"/api/envios/{self.envio_base.id_envio}/"

    def test_listar_envios(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_obtener_detalle_envio(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["numero_guia"], "GUIA-TEST-001")

    def test_crear_envio(self):
        data = {
            "numero_guia": "GUIA-TEST-002",
            "id_usuario": 2,
            "id_empresa": 1,
            "direccion_origen": "Avenida 10 # 20-30",
            "direccion_destino": "Transversal 40 # 50-60",
            "destinatario_nombre": "Maria Gomez",
            "destinatario_telefono": "3109876543",
            "estado": "pendiente",
            "costo_envio": "20000.00",
            "activo": 1
        }
        response = self.client.post(self.url_list, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["numero_guia"], "GUIA-TEST-002")

    def test_actualizar_envio_completo(self):
        data = {
            "numero_guia": "GUIA-TEST-001",
            "id_usuario": 1,
            "id_empresa": 1,
            "direccion_origen": "Calle 1 # 2-3 Modificada",
            "direccion_destino": "Carrera 4 # 5-6",
            "destinatario_nombre": "Juan Pérez",
            "destinatario_telefono": "3001234567",
            "estado": "en_transito",
            "costo_envio": "18000.00",
            "activo": 1
        }
        response = self.client.put(self.url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["direccion_origen"], "Calle 1 # 2-3 Modificada")
        self.assertEqual(response.data["estado"], "en_transito")

    def test_actualizar_estado_parcial(self):
        data = {"estado": "entregado"}
        response = self.client.patch(self.url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["estado"], "entregado")

    def test_eliminar_envio(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Envio.objects.filter(id_envio=self.envio_base.id_envio).exists())

    def test_guia_duplicada_no_permitida(self):
        data = {
            "numero_guia": "GUIA-TEST-001",
            "id_usuario": 3,
            "direccion_origen": "Calle A",
            "direccion_destino": "Calle B",
            "destinatario_nombre": "Carlos",
            "destinatario_telefono": "3000000000",
        }
        response = self.client.post(self.url_list, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
