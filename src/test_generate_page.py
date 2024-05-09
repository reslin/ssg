import unittest
from generate_page import (
    extract_title,
)


class TestGeneratePage(unittest.TestCase):
    def test_extract(self):
        md = "# header"
        self.assertEqual(extract_title(md), "header")


if __name__ == "__main__":
    unittest.main()