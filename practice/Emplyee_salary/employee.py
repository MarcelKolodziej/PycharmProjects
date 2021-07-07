class Employee():
    """Collect name, last name, default salary $5,000"""

    def __init__(self, first_name, last_name, salary):
        """Initilize the employee"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give default salary $5,000"""
        self.salary += amount
