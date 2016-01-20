from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from subprocess import call

PORT = 9000

class ScreenshotHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		file_name = self.headers.getheader('filename', 'screenshot')
		print "Creating screenshot called " + file_name
		screenshot(file_name)
		return self.dump_screenshot_response(file_name)
		
	def do_GET(self):
		print "GET operation not supported!"

	def dump_screenshot_response(self, file_name):
		return {"file":file_name}

	def screenshot(self, name):
		call(["./screenshot.sh", name])
		pass


server = HTTPServer(('', PORT), ScreenshotHandler)
print "serving at port", PORT
server.serve_forever()