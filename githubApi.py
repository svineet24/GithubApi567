"""
@author: Vineet Singh
@date: February 19, 2019
this program implements the functionality to print github repository
and number of commits in that repository
"""

import requests, json

def getRepoCommits(userId):
    """ this method take github username as input and 
    returns repository name and number of commits against that repository """

    try:
        gitURL = f'https://api.github.com/users/{userId}/repos'
    except requests.exceptions.InvalidURL:
        print('URL is invalid!')
    except requests.exceptions.ConnectionError:
        print('Invalid Request!')
    except requests.exceptions.InvalidSchema:
        print('Invalid Request!')
    else:
        response = requests.get(gitURL)
        responseCode = response.status_code
        if  responseCode == 200:
            repositories = json.loads(response.content) # returns list of repositories
            repoData = list()

            for repo in repositories: # x is dict
                repoName = repo['name']
                repoURL = f'https://api.github.com/repos/{userId}/{repoName}/commits'
                commits = requests.get(repoURL)
                commits = json.loads(commits.content) # returns list of commits
                numCommits = len(commits)
                repoData.append(f'Repo: {repoName}, Number of commits: {numCommits}')

            return repoData


# userId = input('Enter user id: ')
userId = 'bunny87'
res = getRepoCommits(userId)

print(res)

if res != None:
    for i in res:
        print(i)
else:
    print('Invalid Request!')
