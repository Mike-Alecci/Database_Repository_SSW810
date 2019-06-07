import unittest
import os
from Final_Exam import SensorInfo

class MichaelsHomeworkTest(unittest.TestCase):
    """Tests that my homework works properly"""

    def test_bad_inputs(self):
        """This tests that my class handles inproper inputs properly"""
        x = os.getcwd()
        self.assertRaises(NotADirectoryError, SensorInfo, "Fake dir, I dont exist")
        x = os.getcwd()

    def test_generate_pretty_table_summaries(self):
        """This tests that my sensor table is created properly"""
        test_list = [["light", 5, 494.0, 156, 861, 5], ["rainfall", 4, 569.8, 259, 800, 4]] #taken directly from canvas
        sensor = SensorInfo("Final Exam/IOT_test")
        for offset, testline in enumerate(sensor.generate_sens_pretty_tables()):
            self.assertEqual(test_list[offset], testline)
        test_list1 = [["light", "Sun", 1, 861.0, 861, 861, 1], ["light", "Mon", 4, 402.2, 156, 542, 4],
                     ["rainfall", "Sun", 3, 570.3, 259, 800, 3], ["rainfall", "Mon", 1, 568.0, 568, 568, 1]] #taken directly from canvas
        for offset, testline in enumerate(sensor.generate_sens_day_pretty_tables()):
            self.assertEqual(test_list1[offset], testline)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)