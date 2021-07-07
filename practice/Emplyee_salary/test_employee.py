import unittest

from employee import Employee
# Define employee give salary
class TestEmployee(unittest.TestCase):
    """Test for the module employee"""

    def setUp(self):
        """Make an employee to use in test"""
        self.marcel = Employee('marcel', 'kolo', 65000)

    def test_give_default_raise(self):
        """test that default raise works correctly"""
        self.marcel.give_raise()
        self.assertEqual(self.marcel.salary, 70000)

    def test_give_coustom_raise(self):
        """Test that coustom raise works correctly"""
        self.marcel.give_raise(10000)
        self.assertEqual(self.marcel.salary, 75000)

if __name__ == '__main__':
    unittest.main()

