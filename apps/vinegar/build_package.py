import os
import random
import shutil
import sys
import setup_project
import tarfile

join = lambda a,*p: os.path.abspath(os.path.join(a,*p))
WORKING_DIR = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = join(WORKING_DIR, 'base')
TEMP_DIR = join(WORKING_DIR, 'tmp')

def write_requirements(project_dir, packages):
    requirements = os.path.join(project_dir, 'requirements.txt')
    with open(requirements, 'w') as fh:
        fh.write("\n".join(packages))

def compress(project_dir, project_name):
    t = tarfile.open(name="%s.tar.gz" % os.path.join(TEMP_DIR,project_name), mode='w:gz')
    t.add(project_dir, recursive=False)
    t.close()
    return os.path.join(TEMP_DIR, "%s.tar.gz" % project_name)

def bundle(project_name, packages):
    project_dir = join(TEMP_DIR, project_name)
    assets_dir = join(project_dir, 'assets')
    setup_project.copy_site(project_name, project_dir)
    write_requirements(assets_dir, packages)
    tar_name = compress(project_dir, project_name)
    return tar_name
