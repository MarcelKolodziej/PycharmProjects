import unittest

from city_functions import get_formatted_city


class CityTestCase(unittest.TestCase):
    """Test for city_function.py"""

    def test_get_formatted_city(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_city = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago Chile')

    def test_city_country_population(self):
        """Add 3 parameter - population wich is optional """
        formatted_city = get_formatted_city('santiago', 'chile', '200000' )
        self.assertEqual(formatted_city, 'Santiago Chile 200000')


if __name__ == '__main__':
    unittest.main()