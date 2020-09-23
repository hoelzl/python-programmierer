# Code a HTTP Server here...
from http.server import HTTPServer, SimpleHTTPRequestHandler

httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()

