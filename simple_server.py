import os
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from subprocess import call

PORT = 9000

class ScreenshotHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		file_name = self.headers.getheader('filename', 'screenshot')
		self.screenshot(file_name)
		return self.dump_screenshot_response(file_name)
		
	def do_GET(self):
		print "GET operation not supported!"

	def dump_screenshot_response(self, file_name):
		return {"file":file_name}

	def screenshot(self, name):
		call(["./screenshot.sh "+ name], shell=True)

server = HTTPServer(('', PORT), ScreenshotHandler)
print "Android CI Bridge serving at port: ", PORT
server.serve_forever()

# if __name__ == "__main__":
# 	current_dir = os.path.dirname(os.path.realpath(__file__))
# 	screenshot_file = os.path.join(current_dir, 'screenshot.sh')
# 	call([screenshot_file + " lalalal"], shell=True)