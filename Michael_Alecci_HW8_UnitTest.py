import unittest
from Michael_Alecci_HW8 import scanning_dir_files
import os
from prettytable import PrettyTable

class MichaelsHomeworkTest(unittest.TestCase):
    """Tests that my homework works properly"""
    def test_scanning_dir_files(self):
        """Tests that my scanning_dir_files works properly"""
        l = [["0_defs_in_this_file.py", "Yes", 0, 0, 3, 57], ["file1.py", "Yes", 2, 4, 25, 270], 
              ["hello.py", "Yes", 0, 0, 1, 21], ["MichaelAlecci_HW1.py", "Yes", 0, 5, 70, 2819],
              ["Michael_Alecci_HW3.py", "Yes", 2, 24, 224, 7775], ["Michael_Alecci_HW4.py", "Yes", 2, 21, 202, 7828],
              ["Michael_Alecci_HW5.py", "Yes", 1, 12, 105, 4578], ["Michael_Alecci_HW6.py", "Yes", 1, 6, 56, 2702],
              ["Michael_Alecci_HW7.py", "Yes", 1, 10, 89, 3710], ["Michael_Alecci_HW8.py", "Yes", 0, 2, 66, 2734],
              ["Michael_Alecci_HW8_UnitTest.py", "Yes", 1, 1, 20, 1216], ["Michael_Alecci_Tim_Shine_HW2.py", "Yes", 1, 10, 119, 5785],
              ["Quiz_testing.py", "Yes", 0, 0, 3, 66], ["TestingInput.py", "Yes", 0, 2, 9, 126]]
        self.assertEqual(scanning_dir_files(os.getcwd()), l)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)