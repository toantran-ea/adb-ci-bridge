import os
import urlparse
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from subprocess import call
try:
    import simplejson
except ImportError:
    import json as simplejson


PORT = 9001
ACTION_UNLOCK = "unlock"
ACTION_SCREENSHOT = "screenshot"
PARAM_TAG = "tag"
PARAM_TRACE = "trace"

class ScreenshotHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		real_path = self.get_path(self.path)
		if real_path.endswith(ACTION_UNLOCK):
			self.unlock()
		elif real_path.endswith(ACTION_SCREENSHOT):
			data_string = self.rfile.read(int(self.headers['Content-Length']))
			data = simplejson.loads(data_string)
			print data
			tag = data.get(PARAM_TAG, "defaulttag")
			trace = data.get(PARAM_TRACE, "")
			print "tag ", tag
			print "trace ", trace
			self.screenshot(tag, trace)

		self.write_header_response_200()
	def do_GET(self):
		print "GET operation not supported!"
		self.send_error(404)
		return

	def get_path(self, query_path):
		return urlparse.urlparse(query_path).path

	def write_header_response_200(self):
		self.send_response(200)
		self.end_headers()

	def screenshot(self, tag, trace):
		call(["./screenshot.sh "+ tag + " \"" + trace + "\""], shell=True)

	def unlock(self):
		call(["./unlock.sh"], shell=True)

server = HTTPServer(('', PORT), ScreenshotHandler)
print "Android CI Bridge serving at port: ", PORT
server.serve_forever()
