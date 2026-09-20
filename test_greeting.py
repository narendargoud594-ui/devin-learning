import unittest
from greeting import greet, goodbye, is_valid_name, format_customer_id


class TestGreeting(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("John"), "Hello, John!")
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet(""), "Hello, !")

    def test_goodbye(self):
        self.assertEqual(goodbye("John"), "Goodbye, John!")
        self.assertEqual(goodbye("Alice"), "Goodbye, Alice!")
        self.assertEqual(goodbye(""), "Goodbye, !")

    def test_is_valid_name(self):
        self.assertTrue(is_valid_name("John"))
        self.assertTrue(is_valid_name("Alice"))
        self.assertTrue(is_valid_name("  John  "))
        self.assertFalse(is_valid_name(""))
        self.assertFalse(is_valid_name("   "))
        self.assertFalse(is_valid_name("\t\n"))

    def test_format_customer_id(self):
        self.assertEqual(format_customer_id("12345"), "Customer ID: 12345")
        self.assertEqual(format_customer_id("ABC123"), "Customer ID: ABC123")
        self.assertEqual(format_customer_id(""), "Customer ID: ")


if __name__ == "__main__":
    unittest.main()
