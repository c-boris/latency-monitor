import unittest
from main import format_url

class TestFormatUrl(unittest.TestCase):
    def test_format_url(self):
        self.assertEqual(format_url("https", "google.com", "/fr"), "https://google.com/fr")
        self.assertEqual(format_url("http", "example.com", "/test"), "http://example.com/test")

if __name__ == "__main__":
    unittest.main()
