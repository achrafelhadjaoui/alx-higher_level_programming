#!/usr/bin/python3

import unittest
from models.base import Base


class test_base(unittest.TestCase):
    """Represent of test_base"""
    def test_task1(self):
        """ test the value of the instance
            public attribute
        """
        obj = Base()
        self.assertEqual(obj.id, 1)
        obj1 = Base(25)
        obj2 = Base()
        self.assertEqual(obj1.id, 25)
        self.assertEqual(obj2.id, 2)


if __name__ == "__main__":
    unittest.main()
