

import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
  
  def setUp(self):
    '''
    Tests behaviour of source class
    '''
    
    self.new_source = Sources('abc','abc_news','Your trusted source for breaking news','abc.com','general','english','us')
    
  def test_instance(self):
    self.assertTrue(isinstance(self.new_source,Sources))  