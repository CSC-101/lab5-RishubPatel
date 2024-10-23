import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    pass
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3

    def test_time_add_1(self):
        time1 = data.Time(1, 1, 1)
        time2 = data.Time(59, 59, 59)
        result = lab5.time_add(time1, time2)
        expected = data.Time(61, 1, 0)
        self.assertEqual(result, expected)

    def test_time_add_2(self):
        time1 = data.Time(7, 4, 23)
        time2 = data.Time(2, 7, 46)
        result = lab5.time_add(time1, time2)
        expected = data.Time(9, 12, 9)
        self.assertEqual(result, expected)

    # Part 4

    def test_is_descending_1(self):
        list1 = [9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 1.0, 2.0]
        result = lab5.is_descending(list1)
        expected = False
        self.assertEqual(result, expected)

    def test_is_descending_2(self):
        list2 = [9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
        result = lab5.is_descending(list2)
        expected = True
        self.assertEqual(result, expected)

    def test_is_descending_3(self):
        list3 = [9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 4.0, 2.0, 1.0]
        result = lab5.is_descending(list3)
        expected = False
        self.assertEqual(result, expected)

    # Part 5

    def test_largest_between_1(self):
        numlist1 = [5, 4, 7, 6, 5, 4, 3, 2, 9, 1]
        result = lab5.largest_between(numlist1, 4, 8)
        expected = 8
        self.assertEqual(result, expected)

    def test_largest_between_2(self):
        numlist2 = [7, 5, 4, 1, 9, 3, 16]
        result = lab5.largest_between(numlist2, 2, 9)
        expected = None
        self.assertEqual(result, expected)

    # Part 6

    def test_furthest_from_origin_1(self):
        points = [data.Point(0,0), data.Point(7, 14), data.Point(99, -99), data.Point(0, 0)]
        result = lab5.furthest_from_origin(points)
        expected = 2
        self.assertEqual(result, expected)

    def test_furthest_from_origin_2(self):
        points = []
        result = lab5.furthest_from_origin(points)
        expected = None
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
