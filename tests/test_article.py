import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    def setUp(self):
        self.new_article = Articles()

    def instance_test(self):
        self.assertTrue(isinstance(self.new_article,Articles))

if __name__ == "__main__":
    unittest.main()