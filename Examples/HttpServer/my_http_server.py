# Code a HTTP Server here...
from http.server import HTTPServer, SimpleHTTPRequestHandler

httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()