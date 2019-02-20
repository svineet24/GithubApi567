"""
@author: vineet singh
@date: February 19, 2019
The primary goal of this file is to demonstrate a simple unittest implementation
"""

import unittest
from HW04 import getRepoCommits, res

# This code implements the unit test functionality

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testgetRepoCommits_Blank(self):
        self.assertEqual(getRepoCommits(''), None)

    def testgetRepoCommits_InvalidValue(self):
        self.assertEqual(getRepoCommits('Test'), None)

    def testgetRepoCommits_ValidValue(self):
        self.assertEqual(getRepoCommits('bunny87'), res)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()