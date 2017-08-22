
import sh
from constants import REPOSITORY_URL, TARGET_FOLDER

git = sh.git.bake(_cwd=TARGET_FOLDER)
git_crypt = sh.git_crypt.bake(_cwd=TARGET_FOLDER)

def install():
    git_crypt_init()
    scaffhold_files()

def git_crypt_init():
    wait(git.init())
    wait(git.remote.add('origin', REPOSITORY_URL))
    wait(git_crypt.init())
    wait(git_crypt('add-gpg-user', '33D1CE78'))

def scaffhold_files():
    sh.mkdir(TARGET_FOLDER + '/content')
    sh.cp('resources/gitattributes.example', TARGET_FOLDER + '/.gitattributes')

def wait(cmd):
    cmd.wait()

if __name__ == '__main__':
    install()
