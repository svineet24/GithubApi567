import unittest

from HW4A_AdityaMunot import *
from unittest import mock


def call_this_one(url):

    if url == 'https://api.github.com/users/AdityaMunot/repos':
        return call('repos1.json')
    elif url == "https://api.github.com/repos/AdityaMunot/Anagram-Variety/commits":
        return call('commitsAnagram-Variety.json')
    elif url == "https://api.github.com/repos/AdityaMunot/hello-world/commits":
        return call('commitshello-world.json')
    elif url == "https://api.github.com/repos/AdityaMunot/RepoFetch/commits":
        return call('commitsRepoFetch.json')
    elif url == "https://api.github.com/repos/AdityaMunot/Repositoryprogram/commits":
        return call('commitsRepositoryprogram.json')
    elif url == "https://api.github.com/repos/AdityaMunot/SSW-555-Group-Project/commits":
        return call('commitsSSW-555-Group-Project.json')
    elif url == "https://api.github.com/repos/AdityaMunot/SSW567/commits":
        return call('commitsSSW567.json')
    elif url == "https://api.github.com/repos/AdityaMunot/Triangle567/commits":
        return call('commitsTriangle567.json')
    elif url == "https://api.github.com/repos/AdityaMunot/AWS-MERN/commits":
        return call('commitsAWS-MERN.json')


def call(path):
    data = Myclass()
    with open(path, 'r') as f:
        data.text = json.load(f)
    return data


class Myclass:
    text = ""


class testrepos(unittest.TestCase):

    @mock.patch('requests.get')
    def testrepos(self, mocked_request):
        mocked_request.side_effect = call_this_one

        repos = Repocheck('AdityaMunot')
        expect = [['Anagram-Variety', 14], ['AWS-MERN', 6], ['hello-world', 3], ['RepoFetch', 16], ['Repositoryprogram', 9], ['SSW-555-Group-Project', 30], ['SSW567', 1], ['Triangle567', 6]]
        self.assertEqual(repos, expect)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
