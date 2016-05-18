#!/usr/bin/env python
import os
import subprocess
import sys
from argparse import ArgumentParser
from shutil import copyfile

#$ sudo pip install --upgrade --no-deps --force-reinstall <packagename>

def get_project_dir():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def recursive_overwrite(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                recursive_overwrite(os.path.join(src, f),
                                    os.path.join(dest, f),
                                    ignore)
    else:
        copyfile(src, dest)

def activate_env():
    #source "${PROJECT_PATH}env34/bin/activate";
    #execfile(activate_this_file, dict(__file__=activate_this_file))
    #subprocess.Popen([venv_python_file, script_file])
    from subprocess import call
    call(["ls", "-l"])
    pass


def de_activate_env():
    #deactivate;
    #execfile(activate_this_file, dict(__file__=activate_this_file))
    pass


PROJECT_PATH = get_project_dir()  # '/home/ubuntu/workspace/'
print("[-] Working on Project at {}".format(PROJECT_PATH))
def clean():
    print('[*] Cleaning Package')
    # todo implement this
    pass

def cp(s,d):
    print('[*] Copying package files from \n\t{} to \n\t{} '.format(s,d))
    recursive_overwrite(s, d)
    print('[*] Copying finished')

def build():
    print('[*] Building Package')
    subprocess.call(['python', PROJECT_PATH+'/django-pa/setup.py', 'sdist'])
    print('[*] Finish Building Package')


def install():
    #todo add sudo -H flag
    print('[*] Uninstalling Package')

    string = "echo y|pip uninstall pa"
    os.system(string)

    print('[*] Finnish Uninstalling Package')
    print('[*] Installing Package')
    subprocess.call(['python', PROJECT_PATH+'/django-pa/setup.py', 'install'])
    print('[*] Finish Installing Package')


def redeploy():
    print('[*] Start redeploy')

    activate_env()
    cp()
    build()
    install()

    de_activate_env()
    print('[*] End redeploy')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-i", help="Install package",action="store_true")
    parser.add_argument("-r", help="Redeploy package",action="store_true")
    parser.add_argument("-c", type=str, help="Copy package",choices=['u','d'])
    parser.add_argument("-b", help="Build package",action="store_true")
    parser.add_argument("-clean", help="Clean package",action="store_true")
    parser.add_argument("-q", "--quiet",
                        action="store_false", dest="verbose", default=True,
                        help="don't print status messages to stdout")

    args = parser.parse_args()
    print(args)
    if args.clean:
        clean()
    if args.r:
        redeploy()
    else:
        if args.c:
            src = PROJECT_PATH+'/testing_prj/package_dev'
            dst = PROJECT_PATH+'/django-pa/pa/'
            cp(src,dst) if args.c == 'u' else cp(dst,src)
        if args.b:
            build()
        if args.i:
            install()
