import os
import sys
from argparse import ArgumentParser
from django.core.management.base import BaseCommand, CommandError


from ._pyckstart import Pyckstart
from django.utils.termcolors import make_style


def get_project_dir():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

#$ sudo pip install --upgrade --no-deps --force-reinstall <packagename>


class Command(BaseCommand):
    help = 'Create and Easily Manage your Django Packages'
    
    
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.style.SUCCESS = make_style(opts=('bold',), fg='green')
        

    def add_arguments(self, parser):
        # Named (optional) arguments
          
        parser.add_argument("-d", "--debug", dest="debug", action="store_true", default=False, help="Enable debug output")
        parser.add_argument("-q", "--quiet", dest="quiet", action="store_true", default=False, help="Disable output")
    
        #parser.add_argument("-v", "--version", dest="version", action="store", type=str, default="0.0.0.0", help="Module version")
        parser.add_argument("-t", "--tests", dest="with_tests", action="store_true", default=False, help="Create tests layout")
        parser.add_argument("-g", "--git", dest="with_git", action="store_true", default=False, help="Enable git repo creation")
        parser.add_argument("-c", "--cli", dest="with_cli", action="store_true", default=False, help="Create CLI layout")
    
        parser.add_argument("-p", "--pyversion", dest="py_version", action="store", default=sys.version_info.major, help="Python version for #!/usr/bin/env python#. Default value : current python major version (%s)" % sys.version_info.major)
        parser.add_argument(
            "-n", 
            "--new", 
            dest="app_name", 
            action="store", 
            default=None,
            help="App name")
    
        parser.add_argument("-it", "--install_templates", dest="install", action="store_true", default=False, help="Install templates in home folder")
        parser.add_argument("-f", "--force", dest="force", action="store_true", default=False, help="Will override existing files. Use with care.")
    
            
        #parser.add_argument("-a", type=str, help=" Name")
        parser.add_argument("-i", help="Install package",action="store_true")
        parser.add_argument("-r", help="Redeploy package",action="store_true")
        parser.add_argument("-cp", type=str, help="Copy package",choices=['u','d'])
        parser.add_argument("-b", help="Build package",action="store_true")
        parser.add_argument("-clean", help="Clean package",action="store_true")
    
    def handle(self, *args, **options):
        
        if options['app_name'] is None :
                self.stdout.write(self.style.ERROR("You must provide an app name. See --help"))
        
        p = Pyckstart(self,options)
        if options['install']:
            p.install_templates()
        else:
            if options['app_name']:p.create_module()
            if options['clean']:p.clean()
            if options['r']:p.redeploy()
            if options['cp']:p.copy_pde(options['c'])
            if options['b']:p.build()
            if options['i']:p.install()
                
    
        
