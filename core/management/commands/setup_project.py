import os
import re
import shutil
import sys

def copy_site(name):
    """
    Copies the project_template directory structure.

    """
    # destination = '/Users/jonathan/projects/'
    destination = ''

    top_dir = os.path.join(destination, name)
    os.mkdir(top_dir)

    project = os.path.abspath(os.path.dirname(__file__))
    template_dir = os.path.join(project, '../../../src/project_template')

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
            fp_new.write(fp_old.read().replace('{{ project_name }}', name))
            fp_old.close()
            fp_new.close()
            try:
                shutil.copymode(path_old, path_new)
            except OSError:
                sys.stderr.write("Error, something bad happened.")

def main():
    if len(sys.argv) < 1:
        p.error("You must specify a project name.")
        sys.exit(0)

    name = sys.argv[1]

    if not os.path.exists(name):
        copy_site(name)
    else:
        print "Project '%s' already exists. Aborting..." % name

if __name__ == '__main__':
	main()
