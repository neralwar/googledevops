#Test Script
import unittest
class TestMainClass(unittest.TestCase):
    def test_addnumber(self):
        self.assertEquals(Mainclass.addnumber(4,5),9)
       
    def test_subnumber(self):
        self.assertEqual(Mainclass.subnumber(8,3),9)
   

if __name__ == '__main__':
    unittest.main()