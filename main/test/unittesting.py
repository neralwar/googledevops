#Test Script
import unittest

class TestMainClass(unittest.TestCase):
    def test_addnumber(self):
        print("FIRST TEST")
        self.assertEquals(5,9)
       
    def test_subnumber(self):
        print("SECOND TEST")
        self.assertEqual(5,5)
   

if __name__ == '__main__':
    unittest.main()