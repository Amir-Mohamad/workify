

import imp


import os
import sys


sys.path.insert(۰, os.path.dirname(__file__))
wsgi = imp.load_source('wsgi', 'config/wsgi.py')
application = wsgi.application
