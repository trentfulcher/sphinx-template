import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(4) == 5
