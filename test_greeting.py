import unittest
from greeting import greet, goodbye


class TestGreeting(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("John"), "Hello, John!")
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet(""), "Hello, !")

    def test_goodbye(self):
        self.assertEqual(goodbye("John"), "Goodbye, John!")
        self.assertEqual(goodbye("Alice"), "Goodbye, Alice!")
        self.assertEqual(goodbye(""), "Goodbye, !")


if __name__ == "__main__":
    unittest.main()
