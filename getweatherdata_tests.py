import unittest
from unittest.mock import patch
import getweatherdata

class TestWeatherData(unittest.TestCase):

    @patch('requests.get')  # Мокаем запрос в API
    def test_get_weather_data_success(self, mock_get):
        # Создаем пример данных, которые будет возвращать mock
        mock_response = {
            "name": "Chicago",
            "coord": {"lat": 41.8781, "lon": -87.6298},
            "sys": {"country": "US"},
            "main": {"feels_like": 15},
            "timezone": -21600
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Проверка выполнения функции
        result = getweatherdata.get_weather_data("Chicago", my_api_key)
        self.assertEqual(result["name"], "Chicago")
        self.assertEqual(result["coord"], {"lat": 41.8781, "lon": -87.6298})
        self.assertEqual(result["country"], "US")
        self.assertEqual(result["feels_like"], 15)
        self.assertEqual(result["timezone"], "UTC-6.0")

    @patch('requests.get')
    def test_get_weather_data_no_city(self, mock_get):
        # Проверяем, что будет возвращено None при пустом значении города
        result = getweatherdata.get_weather_data("", my_api_key)
        self.assertIsNone(result)

    @patch('requests.get')
    def test_get_weather_data_invalid_city(self, mock_get):
        # Мокаем ответ с ошибкой, как если бы город был не найден
        mock_get.return_value.status_code = 404
        result = getweatherdata.get_weather_data("InvalidCity", my_api_key)
        self.assertIsNone(result)

    @patch('requests.get')
    def test_get_weather_data_with_default_key(self, mock_get):
        mock_response = {
            "name": "Dhaka",
            "coord": {"lat": 23.8103, "lon": 90.4125},
            "sys": {"country": "BD"},
            "main": {"feels_like": 30},
            "timezone": 21600
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = getweatherdata.get_weather_data("Dhaka")
        self.assertEqual(result["name"], "Dhaka")
        self.assertEqual(result["coord"], {"lat": 23.8103, "lon": 90.4125})
        self.assertEqual(result["country"], "BD")
        self.assertEqual(result["feels_like"], 30)
        self.assertEqual(result["timezone"], "UTC+6.0")


if __name__ == "__main__":
    unittest.main()
