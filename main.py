
import sh
import time
from datetime import datetime
from constants import REPOSITORY_URL, TARGET_FOLDER, TIME_FORMAT


git = sh.git.bake(_cwd=TARGET_FOLDER)
git_crypt = sh.git_crypt.bake(_cwd=TARGET_FOLDER)

def repo_has_changes():
    return git.status('--porcelain').stdout != ''

def commit_changes():
    git.add('.')
    git.commit('-m %s' % generate_commit_message())

def push_changes():
    print "pushing changes"
    git.push('-f', 'origin', 'master')

def generate_commit_message():
    now = datetime.now()
    message = 'Saved changes at %s' % now.strftime(TIME_FORMAT)
    print message
    return message

if __name__ == '__main__':
    while True:
        time.sleep(2)
        print repo_has_changes()
        if repo_has_changes():
            commit_changes()
            push_changes()
