# perform multiplication of complex numbers on a complex plane
#  a. Python web server
import http.server
import socketserver

PORT = 80

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        file = open("pd_010302b.html")
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.wfile.write(file.read().encode('utf-8'))

httpd = socketserver.TCPServer(("", PORT), CustomHandler)
print("serving at port", PORT)
httpd.serve_forever()
