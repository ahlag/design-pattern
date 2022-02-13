import unittest

class Test(unittest.TestCase):
    def test_circular_array(self):
        ca = CircularArray([11, 22, 33, 44, 55, 66, 77])
        
        # Rotate to the left five times
        ca.rotate(5)
        
        # Check if the first element is 66 after rotating to the left five times
        self.assertEqual(ca[0], 66)
        
        array = []
        for item in ca:
            array.append(item)

        # Check if the array is the same as expected
        self.assertEqual(array, [66, 77, 11, 22, 33, 44, 55])
        
        # Substituting the fourth element
        ca[3] = 999
        
        # Deleting the fifth element
        del ca[4]
        
        # Check if the array is the same as expected
        array = []
        for item in ca:
            array.append(item)
        self.assertEqual(array, [66, 77, 11, 999, 44, 55])
        ca.rotate(2)
        
        array = []
        for item in ca:
            array.append(item)
        self.asserEqual(array, [11, 999, 44, 55, 66, 77])

if __name__ == "__main__":
    unittest.main()