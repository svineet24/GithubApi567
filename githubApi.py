"""
@author: Vineet Singh
@date: February 19, 2019
this program implements the functionality to print github repository
and number of commits in that repository
"""

import urllib.request, json

def getRepoCommits(userId):
    """ this method take github username as input and 
    returns repository name and number of commits against that repository """

    try:
        gitURL = f'https://api.github.com/users/{userId}/repos'
        with urllib.request.urlopen(gitURL) as url:
            repositories = json.loads(url.read().decode()) # returns list of repositories
            repoData = list()

            for repo in repositories: # x is dict
                repoName = repo['name']
                repoURL = f'https://api.github.com/repos/{userId}/{repoName}/commits'
                with urllib.request.urlopen(repoURL) as url:
                    commits = json.loads(url.read().decode()) # returns list of commits
                    numCommits = len(commits)
                    repoData.append(f'Repo: {repoName}, Number of commits: {numCommits}')

            return repoData

    except urllib.error.HTTPError:
        print(f'ERROR: Repository with name "{userId}" does not exist!')


# userId = input('Enter user id: ')
userId = 'bunny87'
res = getRepoCommits(userId)

if res != None: 
    for i in res:
        print(i)
