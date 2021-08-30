import unittest

import main

class MainTest(unittest.TestCase):
    def test(self):
        ret = main.hello_world('Test')
        self.assertEqual(ret, 'Hello World! Black')


if __name__ == '__main__':
    unittest.main()