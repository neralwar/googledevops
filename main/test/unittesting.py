#Test Script
import unittest

class TestMainClass(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_addnumber(self):
        
       
        self.assertEquals(3,3)
       
    def test_subnumber(self):
        
        self.assertEquals(2,3)
        
    def tearDown(self):
        pass
   

if __name__ == '__main__':
    unittest.main()
    
  