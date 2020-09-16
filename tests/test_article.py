import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
  
  def setUp(self):
    self.new_article = Articles('abc','general','alexey','police looking for gunman','an article on gunman','abc-news.com/articles','image.article','7th september')
    
  def test_instance(self):
    self.assertTrue(isinstance(self.new_article,Articles))  
    
    
if __name__ == "__main__":
      unittest.main()   