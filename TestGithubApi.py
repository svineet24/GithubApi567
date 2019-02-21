"""
@author: vineet singh
@date: February 19, 2019
The primary goal of this file is to demonstrate a simple unittest implementation
"""

import unittest
from githubApi import getRepoCommits, res

# This code implements the unit test functionality

class TestGitHub(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testgetRepoCommits_Blank(self):
        self.assertIsNone(getRepoCommits(''))

    def testgetRepoCommits_InvalidValue(self):
        self.assertIsNotNone(getRepoCommits('ABC'))

    def testgetRepoCommits_ValidValue(self):
        self.assertEqual(getRepoCommits('bunny87'), ['Repo: CS546, Number of commits: 2', 
                                                    'Repo: SSW567, Number of commits: 2', 
                                                    'Repo: SSW810, Number of commits: 2', 
                                                    'Repo: Triangle567, Number of commits: 16', 
                                                    'Repo: GithubApi567, Number of commits: 14'])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
