import random
import re
import unittest
from redate import ReDate
from datetime import date

class TestReDateGenerator(unittest.TestCase):

    def test_number_range_1(self):
        try:
            ReDate.number_range_regexp(str(510), str(500))
        except ValueError:
            pass
        else:
            fail("expected a ValueError")

    def test_number_range_2(self):
        try:
            ReDate.number_range_regexp(str(10), str(500))
        except ValueError:
            pass
        else:
            fail("expected a ValueError")

    def test_number_range_3(self):
        result = ReDate.number_range_regexp(str(2), str(2))
        self.assertEqual(result, '2')

    def test_number_range_4(self):
        result = ReDate.number_range_regexp(str(2), str(4))
        self.assertEqual(result, '[2-4]')

    def test_number_range_5(self):
        result = ReDate.number_range_regexp(str(21), str(26))
        self.assertEqual(result, '2[1-6]')

    def test_number_range_6(self):
        result = ReDate.number_range_regexp(str(15), str(42))
        self.assertEqual(result, '(1[5-9]|[2-3][0-9]|4[0-2])')

    def test_number_range_7(self):
        result = ReDate.number_range_regexp(str(180), str(390))
        self.assertEqual(result, '(1[8-9][0-9]|2[0-9]{2}|3([0-8][0-9]|90))')

    '''
    def test_number_range_5(self):
        pattern = ReDate.number_range_regexp(str(109), str(733))
        match = re.search(pattern, 'number 734 string')
        self.assertTrue(match is None)
    '''        


if __name__ == '__main__':
    unittest.main()
