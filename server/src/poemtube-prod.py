#!/usr/bin/env python

import os
import sys

# Paths for your web server
#sys.path.insert( 0, "/home1/username/.local/lib/python" )
#sys.path.insert( 0, '/home1/username/.local/lib/python2.6/site-packages' )
#sys.path.insert( 0, '/home1/username/.local/lib/python/site-packages' )
#sys.path.insert( 0, '/usr/lib/python2.6/site-packages' )

import web

from poemtube import urls

app = web.application( urls, globals() )

# Launch as fastcgi
web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)

if __name__ == "__main__":
	app.run()

