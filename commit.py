
import csv
import requests
import json
from github import Github
import uuid
from git import Repo
import subprocess
from datetime import datetime
from scipy.stats import skewnorm
import zmanim
from zmanim.hebrew_calendar.jewish_calendar import JewishCalendar
from zmanim.hebrew_calendar.jewish_date import JewishDate 



def get_skew_int(numValues, maxValue, skewness):
    # number of commits per day is determined on a skewed positive distribution between 0-12
    # positive nums for skewness are right skewed with a positive distribution
    ran = skewnorm.rvs(a = skewness,loc=maxValue, size=numValues)  #Skewnorm function
    ran = ran - min(ran) # shift the set so the minimum value is equal to zero.
    ran = ran / max(ran) # standadize all the values between 0 and 1. 
    ran = ran * maxValue # multiply the standardized values by the maximum value.
    commit_num = int(ran[0]) # first int of the skewed array
    return commit_num

def create_changes():
    # create file if it doesn't exit and adds a new uuid to the file
    with open("changes.txt", "a+") as f:
        delta = uuid.uuid4().hex # new hash that changes status of the file
        f.write(delta + "\n")
    print ("Added line to file with uuid: " + delta) # log for container

def commit():
    # add untracked hash file
    repo = Repo(search_parent_directories=True)
    repo.index.add("changes.txt") # adds file to be staged for commit
    now = datetime.now() # get current day and time
    dt_str = now.strftime("%m/%d/%Y %H:%M:%S") # formatting datetime for commit message
    repo.index.commit(dt_str) # commit the hash file
    return repo

def push(repo):
    # assumption is remote repo and credentials already set up in git config
    origin = repo.remote(name='origin')
    origin.push()

def main():
    '''
    commit_num = get_skew_int(100, 12, 10)
    print ("Number of commits: " + str(commit_num))
    for i in range(commit_num):
        create_changes()
        repo = commit()
    push(repo)
    '''
    # if the day is a current date, then do not run
    # find jewish year, jewish month, and jewish day
    d = JewishDate() # gets current date for hebrew and gregorian calendars, respectively
    jdate = d.jewish_date
    print (jdate)

    today = JewishCalendar(d.jewish_year, d.jewish_month, d.jewish_day)
    print (today)
    yom_tov_type = today.significant_day() # if None, then it's not yomtov
    yom_tov_today = today.is_yom_tov_assur_bemelacha() # if work forbidden, then True

    chan = JewishCalendar(d.jewish_year, 7, 17)
    chanb = chan.significant_day()
    print (chanb)
    print (chan.is_yom_tov_assur_bemelacha())
    print (chan.is_chol_hamoed())
if __name__ == "__main__":
    main()




