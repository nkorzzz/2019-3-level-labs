import unittest
from Lab_1 import structure



class TestStructure(unittest.TestCase):
    def test_of_strucher(self):
        file = "data_file.json"
        result = structure(file)  # Act
        self.assertEqual(result, 1)  # Assert



if __name__ == '__main__':
    unittest.main()