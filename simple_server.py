import os
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from subprocess import call

PORT = 9000
ACTION_UNLOCK = "unlock"
ACTION_SCREENSHOT = "screenshot"
PARAM_FILENAME = "filename"

class ScreenshotHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		action = self.headers.getheader('action', 'unlock') # default action is unlock device screen
		if action == ACTION_SCREENSHOT:
			file_name = self.headers.getheader(PARAM_FILENAME, 'screenshot')
			self.screenshot(file_name)
			self.dump_screenshot_response(file_name)
		elif action == ACTION_UNLOCK:
			self.unlock()
			self.dump_unlock_response()

		
	def do_GET(self):
		print "GET operation not supported!"

	def dump_screenshot_response(self, file_name):
		self.send_response(200)
  		self.send_header("Content-type", "application/json ")
  		self.end_headers()
  		self.wfile.write({"file":file_name})

	def dump_unlock_response(self):
		self.send_response(200)
  		self.send_header("Content-type", "application/json ")
  		self.end_headers()
		self.wfile.write("Unlock screen ok")

	def screenshot(self, name):
		call(["./screenshot.sh "+ name], shell=True)

	def unlock(self):
		call(["./unlock.sh"], shell=True)

server = HTTPServer(('', PORT), ScreenshotHandler)
print "Android CI Bridge serving at port: ", PORT
server.serve_forever()
