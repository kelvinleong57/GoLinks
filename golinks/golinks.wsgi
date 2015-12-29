import sys, os

sys.path.insert (0,'/var/www/golinks')
os.chdir("/var/www/golinks")

from golinks import app as application