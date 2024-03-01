import unittest
from aleatorio import aleatorio
from prueba1 import *

class Test_IncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(aleatorio.devolver(),4)
    
    def test_notnull(self):
        self.assertNotEqual(prueba1.returnNull(),None)
        
    
if __name__ == '__main__':
    unittest.main()