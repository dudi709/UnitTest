from bmi import *
import unittest


class BMITest(unittest.TestCase):
    def test_calcBMI(self):
        
        # action 
        # calcBMI(height, weight)
        result1 = calcBMI(1.79, 63)
        result2 = calcBMI(0, 321)
        result3 = calcBMI(23, 0)
        result4 = calcBMI(3, 88)
        result5 = calcBMI(-8, 1.7)
        result6 = calcBMI(1.55, -66)
        result7 = calcBMI(-1.55, -99)
        

        # expect/assert
        self.assertEqual(result1, 19.662)
        self.assertEqual(result2, "You cannot divide a number by 0")
        self.assertEqual(result3, "Invalid value")
        self.assertEqual(result4, 9.778)
        self.assertEqual(result5, "Invalid value")
        self.assertEqual(result6, "Invalid value")
        self.assertEqual(result7, "Invalid value")

    def test_weightCheck(self):
        
        # action 
        # weightCheck(bmi_value)
        result1 = weightCheck(-9)
        result2 = weightCheck(13)
        result3 = weightCheck(46)
        result4 = weightCheck(0)
        result5 = weightCheck(30)
        result6 = weightCheck(35)
        result7 = weightCheck(18.5)
        result8 = weightCheck(40)
        

        # expect/assert
        self.assertEqual(result1, "Invalid value")
        self.assertEqual(result2, "Underweight")
        self.assertEqual(result3, "Obesity Rank 3")
        self.assertEqual(result4, "Invalid value")
        self.assertEqual(result5, "Obesity Rank 1")
        self.assertEqual(result6, "Obesity Rank 2")
        self.assertEqual(result7, "Normal weight")
        self.assertEqual(result8, "Obesity Rank 3")


if __name__ == '__main__':
    unittest.main()