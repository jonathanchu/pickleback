import ConfigParser
import sys
import os
import subprocess

Config = ConfigParser.ConfigParser()
Config.read('setup.cfg')
join = lambda a,*p: os.path.abspath(os.path.join(a,*p))

def main(argv):
    project_name = Config.get('project','name')
    create_virtualenv(project_name)
    
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
    base_req = os.path.join(working_dir, 'base-requirements.txt')
    easy_install(bin_path, 'pip')
    pip(bin_path, req_file=base_req)

def easy_install(bin_path, package_name):
    f = os.path.join(bin_path, 'easy_install')
    subprocess.call([f, '-U', package_name])

def pip(bin_path, package_name=None, req_file=None):
    f = os.path.join(bin_path, 'pip')
    if package_name:
        subprocess.call([f, 'install', '-U', package_name])
    if req_file:
        subprocess.call([f, 'install', '-U', '-r', req_file])

if __name__ == '__main__':
    main(sys.argv[1:])
