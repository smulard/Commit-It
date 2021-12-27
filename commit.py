import argparse
import csv
import uuid
from git import Repo
from datetime import datetime
from scipy.stats import skewnorm
from zmanim.hebrew_calendar.jewish_calendar import JewishCalendar
from zmanim.hebrew_calendar.jewish_date import JewishDate 

def is_shabbat_or_yt():
    # calculate whether the day is current shabbat or a yom tov with work forbidden
    # returns true bool is shabbat or yt
    # assumption: this will only be run in the morning as to avoid issues with calculating hebrew date based on location/time of day
    d = JewishDate() # gets current date for hebrew and gregorian calendars, respectively
    today = JewishCalendar(d.jewish_year, d.jewish_month, d.jewish_day)
    assur = today.is_assur_bemelacha() # finds out if today is yom tov with assur bemelacha or shabbat
    return assur

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
    # assumption is remote repo and credentials already set up in local git config
    origin = repo.remote(name='origin')
    origin.push()

def main():
    # flag for hebrew cal
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--shomer", dest="shomer", action="store_true", help="If True, then program will not run on Shabbat or Yomim Tovim")
    flag_vals= parser.parse_args()
    shomer = flag_vals.shomer
    print("Shomer is " + str(shomer))

    if shomer: 
        no_work = is_shabbat_or_yt()
        if no_work is False:
            print ("Committing work today")
            commit_num = get_skew_int(100, 12, 10)
            print ("Number of commits: " + str(commit_num))
            for i in range(commit_num):
                create_changes()
                repo = commit()
            push(repo)
        else:
            print("I don't roll on Shabbos (or Yom Tov)")
    else: # run on all days regardless of Jewish calendar
        commit_num = get_skew_int(100, 12, 10)
        print ("Number of commits: " + str(commit_num))
        for i in range(commit_num):
            create_changes()
            repo = commit()
            push(repo)

    
if __name__ == "__main__":
    main()




