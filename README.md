# Commit It

## Run locally
In order to run locally, it operates based on the assumption that github credentials are already setup in the repo.

Clone the repo: \
`git clone https://github.com/smulard/Commit-It.git`

Install requirements: \
`pip3 install -r requirements.txt`

Save recendiations locally for repo. It is recommended to use a Github token instead of a password. \
`git config --local credentials.helper cache`

Run script: \
`python3 commit-it.py`

## Customizations
This program has the option of not committing on Shabbat and Yom Tov. \
To run the program without committing on those days: \
`python3 commit-it.py --shomer`


