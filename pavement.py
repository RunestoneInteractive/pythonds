import paver
from paver.easy import *
from socket import gethostname
import paver.setuputils
paver.setuputils.install_distutils_tasks()


######## CHANGE THIS ##########
project_name = "pythonds"
###############################

# if you want to override the master url do it here.  Otherwise setting it to None
# configures it for the default case of wanting to use localhost for development
# and interactivepython for deployment

master_url = None
if master_url is None:
    if gethostname() == 'web407.webfaction.com':
        master_url = 'http://interactivepython.org'
    else:
        master_url = 'http://127.0.0.1:8000'

master_app = 'runestone'
serving_dir = './build/pythonds'
dest = '../../static'

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./build/"+project_name,
        sourcedir="./_sources/",
        outdir="./build/"+project_name,
        confdir=".",
        project_name = project_name,
        template_args = {
            'course_id':project_name,
            'login_required':'false',
            'appname':master_app,
            'loglevel':10,
            'course_url':master_url,
            'use_services': 'true',
            'python3': 'true',
            'dburl': 'postgresql://bmiller@localhost/runestone',
            'basecourse': 'pythonds',
        }
    )
)

from runestone import build  # build is called implicitly by the paver driver.
