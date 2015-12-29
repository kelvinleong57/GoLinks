import sys, os

sys.path.insert (0,'/var/www/go-links/golinks')
os.chdir("/var/www/go-links/golinks")

from golinks import app as application