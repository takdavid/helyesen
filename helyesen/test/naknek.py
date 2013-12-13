# -*- encoding: utf-8 -*-

import unittest
import helyesen.naknek as naknek

class TestNaknek(unittest.TestCase):

    def test_nak(self):
        self.assertEqual(u'szolgáltatásnak', naknek.say(u'szolgáltatás'))

    @unittest.skip("hosszabbitando")
    def test_anak(self):
        self.assertEqual(u'szolgáltatásának', naknek.say(u'szolgáltatása'))

    def test_nek(self):
        self.assertEqual(u'elvnek', naknek.say(u'elv'))

    @unittest.skip("hosszabbitando")
    def test_enek(self):
        self.assertEqual(u'elvének', naknek.say(u'elve'))


if __name__ == '__main__':
    unittest.main()
