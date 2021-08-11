import unittest
from user_agent_extractor import parse_device_type, parse_browser_type, parse_browser_version

class TestAgentExtractor(unittest.TestCase):

    user_agent = "Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G930F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.0 Chrome/59.0.3071.125 Mobile Safari/537.36"

    def test_device_type(self):
        self.assertEqual(parse_device_type(self.user_agent), 'Mobile')

    def test_browser_type(self):
        self.assertEqual(parse_browser_type(self.user_agent), 'Samsung Internet')

    def test_browser_version(self):
        self.assertEqual(parse_browser_version(self.user_agent), '7.0')

if __name__ == '__main__':
    unittest.main()