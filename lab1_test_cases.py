import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Tests that an input list of None returns a value error"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_returns_values(self):
       """Test that input list that is empty retuns None. Also tests cases where the list contains all the same number, and where there is only one       number in the list"""       
       list1 = [1,2,3,56,3,4]
       self.assertEqual(max_list_iter([1,2,3,56,3,4]),56)
       self.assertEqual(max_list_iter([3,4]),4)
       self.assertEqual(max_list_iter([1,1,1,1]),1)
       self.assertEqual(max_list_iter([21]),21)
       self.assertEqual(max_list_iter([]),None)
    
    def test_reverse_rec(self):
       """Checks if reverse function reverse lists (normal cases) and lists of length 1, as well as empty lists (returns an empty list)"""
       self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
       self.assertEqual(reverse_rec([1,27,68,90,23445,12,2]),[2,12,23445,90,68,27,1])
       self.assertEqual(reverse_rec([1]),[1])
       self.assertEqual(reverse_rec([9,9,9,9]),[9,9,9,9])
       self.assertEqual(reverse_rec([]),[])
    
    def test_reverse_rec_None(self):
        """Tests that an input list of None returns a value error"""
        list = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(list) 

    def test_bin_search(self):
        """Checks that if list_val is not in list (that is searched) the function returns None.
        Also checks if functions can find all values above and below midpoint"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None )
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 1 ) 
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 )
        self.assertEqual(bin_search(3, 0, len(list_val)-1, list_val), 3 )
        self.assertEqual(bin_search(7, 0, len(list_val)-1, list_val), 5 )
        self.assertEqual(bin_search(8, 0, len(list_val)-1, list_val), 6 )
        self.assertEqual(bin_search(9, 0, len(list_val)-1, list_val), 7 )
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8 )

    def bin_search_None(self):
        """Tests that an input list  of None returns a value error"""
        list = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(list)



if __name__ == "__main__":
        unittest.main()


    
