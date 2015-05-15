import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
import os, sys

from sphinxcontrib import paverutils

sys.path.append(os.getcwd())
sys.path.append('../modules')


######## CHANGE THIS ##########
project_name = "pythonds"
###############################

master_url = 'http://127.0.0.1:8000'
master_app = 'runestone'

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./build/"+project_name,
        sourcedir="./source/",
        outdir="./build/"+project_name,
        confdir=".",
        template_args = {
            'course_id':project_name,
            'login_required':'false',
            'appname':master_app,
            'loglevel':10,
            'course_url':master_url,
            'use_services': 'true',
            'python3': 'true',
        }
    )
)

if project_name == "<project_name>":
  print("Please edit pavement.py and give your project a name")
  exit()

@task
@cmdopts([
    ('all','a','rebuild everything'),
    ('outputdir=', 'o', 'output static files here'),
    ('masterurl=', 'u', 'override the default master url'),
    ('masterapp=', 'p', 'override the default master app')
])
def build(options):
    if 'all' in options.build:
      options['force_all'] = True
      options['freshenv'] = True

    try:
        bi = sh('git describe --long',capture=True)[:-1]
        bi = bi.split('-')[0]
        options.build.template_args["build_info"] = bi
    except:
        options.build.template_args["build_info"] = 'unknown'

    if 'outputdir' in options.build:
        options.build.outdir = options.build.outputdir

    if 'masterurl' in options.build:
        options.build.template_args['course_url'] = options.build.masterurl

    if 'masterapp' in options.build:
        options.build.template_args['appname'] = options.build.masterapp

    print('Building into ', options.build.outdir)
    rc = paverutils.run_sphinx(options, 'build')

    try:
        from chapternames import populateChapterInfo
        print('Creating Chapter Information')
        populateChapterInfo(project_name, "%s/index.rst" % options.build.confdir)
    except ImportError:
        print('Chapter information database population skipped, This is OK for a standalone build.')

    if rc == 0:
        print("Done, {} build successful".format(project_name))
    else:
        print("Error in building {}".format(project_name) )
