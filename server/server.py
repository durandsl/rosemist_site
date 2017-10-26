#!/usr/bin/python3
import os
import cherrypy
from sendemail import EmailHandler

PATH = "/var/www/rosemist_site/pages"
LOCAL = os.path.abspath(os.path.dirname(__file__))
class Root(object): pass

cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 80})
cherrypy.tree.mount(Root(), '/', config={
        '/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': PATH,
                'tools.staticdir.index': 'index.html',
                'log.screen': False,
                'log.access_file': LOCAL + '/access.log',
                'log.error_file': LOCAL + '/error.log'
            }
    })
cherrypy.tree.mount(EmailHandler(), '/email' 
        ,config={
        '/' : {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        }
})

cherrypy.engine.start()
cherrypy.engine.block()

