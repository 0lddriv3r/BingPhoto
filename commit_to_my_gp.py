import os
import datetime
import subprocess
import bing_photo
from apscheduler.schedulers.blocking import BlockingScheduler


def commit_to_my_gp():
    date = datetime.datetime.now()
    commit_text = 'Refresh background.jpg on {:%B %d, %Y}'.format(date)

    os.chdir("/Users/JiajieZhuo/Documents/Blog/img")

    status_old = subprocess.call(["git", "status"])
    git_add = subprocess.call(["git", "add", "background.jpg"])
    status_new = subprocess.call(["git", "status"])
    git_commit = subprocess.call(["git", "commit", "-m" + commit_text])
    git_push = subprocess.call(["git", "push"])
    print 'Git push background.jpg successfully!'


def work_flow():
    bing_photo.download_bing_photo()
    commit_to_my_gp()

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(work_flow, 'cron', day_of_week='0-6', hour=6, minute=0)
    scheduler.start()
