import paver
from paver.easy import *
from socket import gethostname
import paver.setuputils
paver.setuputils.install_distutils_tasks()
from os import environ
import pkg_resources

######## CHANGE THIS ##########
project_name = "pythonds"
###############################

# if you want to override the master url do it here.  Otherwise setting it to None
# configures it for the default case of wanting to use localhost for development
# and interactivepython for deployment

master_url = None
if master_url is None:
    if gethostname() == 'runestone-deploy':
        master_url = 'https://runestone.academy'
        doctrees = '../../custom_courses/{}/doctrees'.format(project_name)
    elif environ['RUNESTONE_HOST']:
        master_url = 'http://{}'.format(environ['RUNESTONE_HOST'])
        doctrees = './build/{}/doctrees'.format(project_name)
    else:
        master_url = 'http://127.0.0.1:8000'
        doctrees = './build/{}/doctrees'.format(project_name)

master_app = 'runestone'
dynamic_pages = True
serving_dir = './build/pythonds'
if dynamic_pages:
    dest = './published'
else:
    dest = '../../static'

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./build/"+project_name,
        sourcedir="./_sources/",
        outdir="./build/"+project_name,
        confdir=".",
        project_name = project_name,
        doctrees = doctrees,
        template_args = {
            'course_id':project_name,
            'login_required':'false',
            'appname':master_app,
            'loglevel':10,
            'course_url':master_url,
            'use_services': 'true',
            'dynamic_pages': dynamic_pages,
            'python3': 'true',
            'dburl': 'postgresql://bmiller@localhost/runestone',
            'basecourse': 'pythonds',
            'downloads_enabled': 'false',
            'enable_chatcodes': 'false',
            'allow_pairs': 'false'
        }
    )
)

version = pkg_resources.require("runestone")[0].version
options.build.template_args['runestone_version'] = version

# Check to see if we are building on our Jenkins build server, if so use the environment variables
# to update the DB information for this build
if 'DBHOST' in environ and  'DBPASS' in environ and 'DBUSER' in environ and 'DBNAME' in environ:
    options.build.template_args['dburl'] = 'postgresql://{DBUSER}:{DBPASS}@{DBHOST}/{DBNAME}'.format(**environ)

from runestone import build  # build is called implicitly by the paver driver.
