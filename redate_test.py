import random
import unittest

class TestReDateGenerator(unittest.TestCase):

    
    def test_default_format(self):
        before_date = date(1980, 7, 17)
        after_date = date(2012, 12, 17)
        date_regexp = ReDate(before_date, after_date)
        self.assertEqual(date_regexp.get(), '')






if __name__ == '__main__':
    unittest.main()
