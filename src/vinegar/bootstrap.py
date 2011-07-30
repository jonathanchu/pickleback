import ConfigParser
import sys
import os
import subprocess

Config = ConfigParser.ConfigParser()
Config.read('setup.cfg')
join = lambda a,*p: os.path.abspath(os.path.join(a,*p))
PROJECT_NAME = Config.get('project','name')

def main(argv):
    create_virtualenv(PROJECT_NAME)
    
def detect_active_virtualenv():
    """ check if a virtualenv is currently activated """
    if getattr(sys, 'real_prefix', False):
        return True
    else:
        return False

def get_virtualenv_path():
    """ check if virtualenv is installed on system """
    return os.environ.get('WORKON_HOME', False)

def create_virtualenv(project_name):
    import virtualenv
    workon_path = get_virtualenv_path()
    home_path = join(workon_path, project_name)
    working_dir = os.path.abspath(os.path.dirname(__file__))
    
    virtualenv.create_environment(home_path, site_packages=False, clear=True)
    
    if sys.platform == 'win32':
        bin_dirname = 'Scripts'
    else:
        bin_dirname = 'bin'
    
    bin_path = join(home_path, bin_dirname)
    activate_virtualenv(bin_path)
    base_req = os.path.join(working_dir, 'base-requirements.txt')
    easy_install(bin_path, 'pip')
    pip(bin_path, req_file=base_req)
    django_init(bin_path, PROJECT_NAME)

def easy_install(bin_path, package_name):
    f = os.path.join(bin_path, 'easy_install')
    subprocess.call([f, '-U', package_name])

def pip(bin_path, package_name=None, req_file=None):
    f = os.path.join(bin_path, 'pip')
    if package_name:
        subprocess.call([f, 'install', '-U', package_name])
    if req_file:
        subprocess.call([f, 'install', '-U', '-r', req_file])

def activate_virtualenv(bin_path):
    base = os.path.abspath(os.path.join(bin_path, '../'))
    if sys.platform == 'win32':
        site_packages = os.path.join(base, 'Lib', 'site-packages')
    else:
        site_packages = os.path.join(base, 'lib', 'python%s' % sys.version[:3], 'site-packages')
    prev_sys_path = list(sys.path)
    import site
    site.addsitedir(site_packages)
    sys.real_prefix = sys.prefix
    sys.prefix = base
    
    new_sys_path = []
    for item in list(sys.path):
        if item not in prev_sys_path:
            new_sys_path.append(item)
            sys.path.remove(item)
    sys.path[:0] = new_sys_path

def clean_up(bin_path):
    pass

def django_init(bin_path, project_name=PROJECT_NAME):
    f = os.path.join(bin_path, 'django-admin.py')
    subprocess.call([f, 'startproject', project_name])

if __name__ == '__main__':
    main(sys.argv[1:])
