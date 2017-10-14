#!/usr/bin/python3
import os
import cherrypy

PATH = "/home/stephanie/rosemist_goldens/rosemist_site"
LOCAL = os.path.abspath(os.path.dirname(__file__))
class Root(object): pass

cherrypy.config.update({'server.socket_port': 80})
cherrypy.tree.mount(Root(), '/', config={
        '/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': PATH,
                'tools.staticdir.index': 'index.html',
                'log.screen': False,
                'log.access_file': LOCAL + '/access.log',
                'log.error_file': LOCAL + '/error.log'
            },
    })

cherrypy.engine.start()
cherrypy.engine.block()

