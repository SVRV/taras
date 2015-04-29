activate_this = '/Users/krasilich/projects/python/.virtualenvs/taras/bin/activate_this.py'

execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/Users/krasilich/projects/python/taras')

from main import app as application