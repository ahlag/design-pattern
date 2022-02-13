import unittest

class CircularArray(object):
    
    def __init__(self, array) -> None:
        self.array = array
        self.start = 0

    def rotate(self, i):
        self.start = (self.start + i) % len(self.array)
        
    def __iter__(self):
        for i in range(self.start, len(self.array)):
            yield self.array[i]
        for i in range(0, self.start):
            yield self.array[i]
        
    def __getitem__(self, i):
        return self.array[(self.start + i) % len(self.array)]
    
    def __setitem__(self, i, item):
        self.array[(self.start + i) % len(self.array)] = item

    def __delitem__(self, i):
        index = (self.start + i) % len(self.array)
        del self.array[index]
        if index < self.start:
            self.start -= 1
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
        self.assertEqual(array, [11, 999, 44, 55, 66, 77])

if __name__ == "__main__":
    unittest.main()