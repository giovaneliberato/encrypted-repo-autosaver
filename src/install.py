
import sh
from config import ConfigManager


config = ConfigManager()
git = sh.git.bake(_cwd=config.get("TARGET_FOLDER"))
git_crypt = sh.git_crypt.bake(_cwd=config.get("TARGET_FOLDER"))

def install():
    git_crypt_init()
    scaffhold_files()

def git_crypt_init():
    wait(git.init())
    wait(git.remote.add('origin', config.get("REPOSITORY_URL")))
    wait(git_crypt.init())
    wait(git_crypt('add-gpg-user', config.get("GPG_USER")))

def scaffhold_files():
    sh.mkdir(config.get("TARGET_FOLDER") + '/content')
    sh.cp('resources/gitattributes.example', config.get("TARGET_FOLDER") + '/.gitattributes')

def wait(cmd):
    cmd.wait()

if __name__ == '__main__':
    install()
