#!/usr/bin/python3

import sys
import unittest

from gInt import gInt

class gIntTest(unittest.TestCase):
	'''Test for gInt class'''

	def setUp(self):
		'''Run before tests'''
		self.one = gInt(1, 1)
		self.one_copy = gInt(1, 1)
		self.two = gInt(5, 6)
		self.two_copy = gInt(5, 6)
		self.three = gInt(-5, 10)
		self.three_copy = gInt(-5, 10)
		self.four = gInt(2, -7)
		self.four_copy = gInt(2, -7)
		self.five = gInt(-3, -1)
		self.five_copy = gInt(-3, -1)
		self.rIdentity = gInt(1, 0)
		self.iIdentity = gInt(0, 1)
		self.zero = gInt(0, 0)

	def tearDown(self):
		'''Run after each test if setUp() fails'''
		pass

	def test_add(self):
		sum1 = self.one + self.two
		self.assertEqual(sum1, gInt(6, 7), '(1 + i) + (5 + 6i) failed')
		
		sum1 = self.three + self.four
		self.assertEqual(sum1, gInt(-3, 3), '(-5 + 10i) + (2 - 7i) failed')

		sum1 = self.five + self.rIdentity
		self.assertEqual(sum1, gInt(-2, -1), '(-3 - i) + 1 failed')

		sum1 = self.three + self.iIdentity
		self.assertEqual(sum1, gInt(-5, 11), '(-5 + 10i) + i failed')

		sum1 = self.zero + self.rIdentity + self.iIdentity
		self.assertEqual(sum1, self.one, '(0 + 0i) + 1 + i failed')

	def test_mult(self):
		prod1 = self.iIdentity * self.iIdentity
		self.assertEqual(prod1, gInt(-1, 0), 'i * i failed')

		prod1 = self.rIdentity * self.rIdentity
		self.assertEqual(prod1, gInt(1, 0), '1 * 1 failed')

		prod1 = self.one * self.rIdentity
		self.assertEqual(prod1, prod1, '(1 + i) * 1 failed')

		prod1 = self.one * self.iIdentity
		self.assertEqual(prod1, gInt(-1, 1), '(1 + i) * i failed')

		prod1 = self.one * self.two
		self.assertEqual(prod1, gInt(-1, 11), '(1 + i) * (5 + 6i) failed')

		prod1 = self.three * self.zero
		self.assertEqual(prod1, self.zero, '(-5 + 10i) * (0 + 0i) failed')

		prod1 = self.four * self.five
		self.assertEqual(prod1, gInt(-13, 19), '(2 - 7i) * (-3 - i) failed')

	def test_norm(self):
		norm1 = self.zero.norm()
		self.assertEqual(norm1, 0, '|0 + 0i| failed')

		norm1 = self.rIdentity.norm()
		self.assertEqual(norm1, 1, '|1| failed')
		
		norm1 = self.iIdentity.norm()
		self.assertEqual(norm1, 1, '|i| failed')

		norm1 = self.one.norm()
		self.assertEqual(norm1, 2, '|1 + i| failed')

		norm1 = self.three.norm()
		self.assertEqual(norm1, 125, '|-5 + 10i| failed')

		norm1 = self.five.norm()
		self.assertEqual(norm1, 10, '|-3 - i| failed')

if __name__ == '__main__' :
	sys.argv.append('-v')
	unittest.main()
