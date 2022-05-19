# Code a HTTP Server here...

from http.server import HTTPServer, SimpleHTTPRequestHandler

def run():
	httpd = HTTPServer(("", 8000), SimpleHTTPRequestHandler)
	httpd.serve_forever()

print(f"HTTP Server module name {__name__}.")

if __name__ == "__main__":
	run()
