import unittest

from unit_test.dict import Dict


class TestDict(unittest.TestCase):

    def setUp(self):
        print('setting')

    def tearDown(self):
        print('tearing')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):  #此条件与__getattr__返回的Error需要一致
            value = d.empty

if __name__ == '__main__':
    unittest.main()

