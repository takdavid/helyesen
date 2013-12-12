# -*- encoding: utf-8 -*-

import unittest
import helyesen.az as az

class TestAz(unittest.TestCase):

    def test_a(self):
        self.assertEqual(u'a szolgáltatás', az.say(u'szolgáltatás'))

    def test_az(self):
        self.assertEqual(u'az áramszolgáltatás', az.say(u'áramszolgáltatás'))


if __name__ == '__main__':
    unittest.main()
