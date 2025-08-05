from rest_framework.test import APITestCase
from django.urls import reverse

class HealthTests(APITestCase):
    def test_health(self):
        url = reverse('Health')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "Server is up!"})

class CalculatorEndpointTests(APITestCase):
    def _test_operation(self, op_name, a, b, expected_result):
        url = reverse(op_name.capitalize())
        # Test GET
        response = self.client.get(url, {'a': a, 'b': b})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"result": expected_result})
        # Test POST
        response = self.client.post(url, {"a": a, "b": b}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"result": expected_result})

    def test_add(self):
        self._test_operation('add', 5, 3, 8)

    def test_subtract(self):
        self._test_operation('subtract', 10, 4, 6)

    def test_multiply(self):
        self._test_operation('multiply', 6, 7, 42)

    def test_divide(self):
        self._test_operation('divide', 27, 3, 9)

    def test_missing_params(self):
        url = reverse("Add")
        response = self.client.get(url, {})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.data)

    def test_invalid_params(self):
        url = reverse("Multiply")
        response = self.client.post(url, {"a": "foo", "b": 7}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.data)

    def test_divide_by_zero(self):
        url = reverse("Divide")
        response = self.client.get(url, {"a": 10, "b": 0})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {"error": "Division by zero is not allowed."})
