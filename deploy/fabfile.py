from fabric.api import *

env.hosts = ['178.79.172.91']
env.user = 'root'
env.password = ''

def deploy():
    try:
        run("cd /var/www/pickleback.me/pickleback; git pull origin master")
        run("supervisorctl restart gunicorn")
    except:
        pass

