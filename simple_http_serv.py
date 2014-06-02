#/usr/bin/python

#hikohong@gmail.com

#This is from web sample
#http://www.linuxjournal.com/content/tech-tip-really-simple-http-server-python

import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

#
# usage show
#
def usage_show():
	print "=============================================================="
	print "simple_http_serv [port] <ip: optional>"
	print "port: default 8080 unless you assign a dedicated port number"
	print "ip: optional for the ip address assigned"
	print "=============================================================="
	return

#
# main program
#
Protocol     = "HTTP/1.0"
HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer

if sys.argv[1:]:
	if cmp('--help', sys.argv[1]):
		port = int(sys.argv[1])
	else:
		usage_show()
		sys.exit()
else:
	port = 8000


if sys.argv[2:]:
	server_addr = (sys.argv[2], port)
else:
	server_addr = ('127.0.0.1', port)


HandlerClass.protocol_version = Protocol

httpd = ServerClass(server_addr, HandlerClass)

sa = httpd.socket.getsockname()

print "HTTP server is activating now on", sa[0], "port:", sa[1], "..."

httpd.serve_forever()





