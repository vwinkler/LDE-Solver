import unittest
from parameterized import parameterized
import util

class MergeDictionaryTests(unittest.TestCase):
    @parameterized.expand([
        [{}, {}, {}],
        [{1:1}, {2:2}, {1:1, 2:2}],
        [{1:1}, {1:2}, {1:3}],
        [{1:1}, {1:-2}, {1:-1}],
        [{1:1,2:2}, {1:3,3:4}, {1:4, 2:2, 3:4}],
        [{1:1,2:2}, {1:3,2:5}, {1:4, 2:7}],
        [{1:1}, {}, {1:1}],
        [{}, {2:2}, {2:2}],
        ])
    def test(self, a, b, expected):
        self.assertDictEqual(util.mergeDictionaries(a, b, lambda x, y: x + y), expected)
