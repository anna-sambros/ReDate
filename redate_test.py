import random
import re
import unittest
from redate import ReDate
from datetime import date

class TestReDateGenerator(unittest.TestCase):

    def test_number_range_1(self):
        pattern = ReDate.number_range_regexp(str(109), str(733))
        match = re.search(pattern, 'number 108 string')
        self.assertTrue(match is None)

    def test_number_range_2(self):
        pattern = ReDate.number_range_regexp(str(109), str(733))
        match = re.search(pattern, 'number 109 string')
        self.assertTrue(match is not None)

    def test_number_range_3(self):
        pattern = ReDate.number_range_regexp(str(109), str(733))
        match = re.search(pattern, 'number 555 string')
        self.assertTrue(match is not None)

    def test_number_range_4(self):
        pattern = ReDate.number_range_regexp(str(109), str(733))
        match = re.search(pattern, 'number 733 string')
        self.assertTrue(match is not None)

    def test_number_range_5(self):
        pattern = ReDate.number_range_regexp(str(109), str(733))
        match = re.search(pattern, 'number 734 string')
        self.assertTrue(match is None)




if __name__ == '__main__':
    unittest.main()
