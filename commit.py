
import csv
import requests
import json
from github import Github
import uuid
from git import Repo
import subprocess
import subprocess


# create file if it doesn't exit and adds a new uuid to the file
with open("changes.txt", "a+") as f:
    delta = uuid.uuid4().hex # new hash that changes status of the file
    f.write(delta + "\n")

# add untracked hash file
repo = Repo(search_parent_directories=True)
print(repo) # path of git repo 
adding = subprocess.run(["git", "add", "changes.txt"])

print (adding)

# access creds for github: username, github token, repo url
with open ('creds.txt') as f:
    reader = csv.reader(f, delimiter=",")
    for i, row in enumerate(reader):
        username = row[0]
        token = row[1]
        repo_url = row[2]
        gh_repo = row[3]

#access to github
g = Github(token)




