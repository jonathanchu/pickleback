import os
import random
import re
import shutil
import sys

join = lambda a,*p: os.path.abspath(os.path.join(a,*p))
WORKING_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = join(WORKING_DIR, 'base')

def copy_site(name, destination):
    """
    Copies the project_template directory structure.

    """

    top_dir = destination
    os.mkdir(top_dir)

    project = os.path.abspath(os.path.dirname(__file__))
    template_dir = PROJECT_DIR

    for d, subdirs, files in os.walk(template_dir):
        relative_dir = d[len(template_dir)+1:].replace('project_name', name)
        if relative_dir:
            os.mkdir(os.path.join(top_dir, relative_dir))
        for subdir in subdirs[:]:
            if subdir.startswith('.'):
                subdirs.remove(subdir)
        for f in files:
            path_old = os.path.join(d, f)
            path_new = os.path.join(top_dir, relative_dir, f.replace('project_name', name))
            fp_old = open(path_old, 'r')
            fp_new = open(path_new, 'w')
            fp_new.write(fp_old.read().replace('{{ project_name }}', name).replace('{{ secret_key }}', generate_secret_key()))
            fp_old.close()
            fp_new.close()
            try:
                shutil.copymode(path_old, path_new)
            except OSError:
                sys.stderr.write("Error, something bad happened.")

def generate_secret_key():
    c = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
    return "".join([random.choice(c) for x in xrange(50)])
