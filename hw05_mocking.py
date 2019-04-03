import unittest
import json
from unittest import TestCase
from unittest.mock import patch, call
from githubApi import getRepoCommits
from os import listdir
from os.path import isfile, join

testData = dict()

for f in listdir('data_file'):
    f_name = join('data_file', f)
    if isfile(f_name):
        file = open(f_name, 'r')
        testData[f_name] = json.loads(file.read())
        file.close()

def mock_get_request(*args, **kwargs):
    """ mock_get_request is used for intercepting the requests in the function
    so as to remove the api call limitation on github
    """

    class MockResponse:
        """ class to interpret mock response """

        def __init__(self, json_data, status_code):
            """ class constructor use to intialize the call instances """

            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            """ this method returns the response in json data """

            return self.json_data

    if args[0] == 'https://api.github.com/users/bad-request/repos':
        return MockResponse(None, 500)

    fileName = 'test-data/' + args[0].replace('https://api.github.com/', '').\
        replace('/', '#') + '.json'
    if fileName in testData:
        return MockResponse(testData[fileName], 200)
    
    return MockResponse({'message': 'Not Found', 'documentation_url': 
    'https://developer.github.com/v3/repos/#list-user-repositories'}, 404)

class TestGitHubAPI(TestCase):
    """ class to test github API """

    @patch('requests.get', side_effect = mock_get_request)
    @patch('GitHubAPI.print')
    def testBasic(self, print_, reqs_):
        """ this method verifies the github repository commit counts """

        getRepoCommits('richkempinski')
        self.assertEqual(print_.call_args_list, 
        [
            call('Repo: hellogitworld Number of commits: 30'),
            call('Repo: helloworld Number of commits: 2'),
            call('Repo: Project1 Number of commits: 2'),
            call('Repo: threads-of-life Number of commits: 1')
        ],
        "invalid results for userID 'richkempinski'")
        self.assertEqual(reqs_.call_args_list,
        [
            call('https://api.github.com/users/richkempinski/repos'),
            call('https://api.github.com/repos/richkempinski/hellogitworld/commits'),
            call('https://api.github.com/repos/richkempinski/helloworld/commits'),
            call('https://api.github.com/repos/richkempinski/Project1/commits'),
            call('https://api.github.com/repos/richkempinski/threads-of-life/commits')
        ], "invalid calls for requests when getting 'richkempinski'")

    @patch('requests.get', side_effect = mock_get_request)
    @patch('GitHubAPI.print')
    def testUnknownUserId(self, print_, reqs_):
        """ this method verifies the github repository commit counts """

        getRepoCommits('sdflkjsdflkjsdflkjsdflkjsdflkjsdlfkjsdflkjsdlkjsdf')
        self.assertEqual(print_.call_args_list, [call('UserID not found')], 'userID error check')
        self.assertEqual(reqs_.call_args_list, [call('https://api.github.com/users/\
            sdflkjsdflkjsdflkjsdflkjsdflkjsdlfkjsdflkjsdlkjsdf/repos')], 
            'expected invalid user to be called')

    @patch('requests.get', side_effect = mock_get_request)
    @patch('GitHubAPI.print')
    def testNoReposForUser(self, print_, reqs_):
        """ this method verifies if there is a response from a user or not """

        getRepoCommits('sdfsdfsdfsdfsdfsdf')
        self.assertEqual(print_.call_args_list, [], 'no repos should have been found for the user')
        self.assertEqual(reqs_.call_args_list, [call('https://api.github.com/\
            users/sdfsdfsdfsdfsdfsdf/repos')], 'expected user without any repos to be called')

    @patch('requests.get', side_effect = mock_get_request)
    @patch('GitHubAPI.print')
    def testBadResponses(self, print_, reqs_):
        """ this method checks for bad responses """

        getRepoCommits('bad-request')
        self.assertEqual(print_.call_args_list, [call('Cannot contact github')], \
            'bad request so cannot contact github expected')
        self.assertEqual(reqs_.call_args_list, [call('https://api.github.com/users/bad-request/repos')], 
        'expected bad-request to be called only')

    @patch('requests.get', side_effect = mock_get_request)
    @patch('GitHubAPI.print')
    def testInvalidInput(self, print_, reqs_):
        """ this method verifies the input types """

        getRepoCommits(1)
        self.assertEqual(print_.call_args_list, [call('Input must be a string')], 
            'invalid input so input must be string expected')
        self.assertEqual(reqs_.call_args_list, [], 'invalid input so no calls expected')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
