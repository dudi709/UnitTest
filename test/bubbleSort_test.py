from bubbleSort import *
import unittest


class bubbleSortTest(unittest.TestCase):
    def test_bubbleSort(self):
        
        # stub
        stub1 = [7, -4, 3, 6]
        stub2 = [99, 0, -66, 100, 1]
        stub3 = []
        stub4 = [0, 1, 2, 3, 4, 5]

        # assume
        expected1 = [-4, 3, 6, 7]
        expected2 = [-66, 0, 1, 99, 100]
        expected3 = []
        expected4 = [0, 1, 2, 3, 4, 5]
        
        # action
        result1 = bubbleSort(stub1)
        result2 = bubbleSort(stub2)
        result3 = bubbleSort(stub3)
        result4 = bubbleSort(stub4)
 
        # expect/assert
        self.assertEqual(result1, expected1) #Check whether the array is sorted and we lost no value
        self.assertEqual(len(result1), len(expected1)) #Check whether the array is sorted and we lost no value
        self.assertEqual(result2, expected2) #Check whether the array is sorted and we lost no value
        self.assertEqual(result3, expected3) #Check whether the array is sorted and we lost no value
        self.assertEqual(result4, expected4) #Check whether the array is sorted and we lost no value
        self.assertIsNotNone(result1) #Check whether the function returns a value
        self.assertIsNotNone(result2) #Check whether the function returns a value
        self.assertIsNotNone(result3) #Check whether the function returns a value
        self.assertIsNotNone(result4) #Check whether the function returns a value
        
        

        
if __name__ == '__main__':
    unittest.main()
        
        