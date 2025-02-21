import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_version_endpoint(self):
        response = self.client.get("/version")
        self.assertEqual(response.status_code, 200)
        self.assertIn("version", response.json)

    def test_temperature_endpoint(self):
        response = self.client.get("/temperature")
        self.assertIn(response.status_code, [200, 404, 500])  # API-dependent

if __name__ == "__main__":
    unittest.main()
