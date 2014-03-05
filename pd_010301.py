# express a complex number in Cartesian and polar representations
import math
import re
import http.server
import socketserver

PORT = 80

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')

        text = """
         <html>
          <body>
           <form action="convert" method="get">
            <input type="text" name="q1">
            <input type="text" name="q2">
            <input type="submit" value="Convert">
           </form>"""

        parms = re.search("q1=([0-9.]*)&q2=([0-9.]*)", self.path)
        if parms:
            q1 = float(parms.group(1))
            q2 = float(parms.group(2))

            md = math.sqrt(q1 ** 2 + q2 ** 2)
            ang = math.atan(q2 / q1)
            text += "\n(&rho;, &theta;) = ( " + str(md) + ", " + str(ang) + " )<br>"

            a = q1 * math.cos(q2)
            b = q1 * math.sin(q2) 
            text += "\n(a, b) = ( " + str(a) + ", " + str(b) + " )"

        text += """
          </body>
         </html>"""
 
        self.wfile.write(text.encode('utf-8'))

httpd = socketserver.TCPServer(("", PORT), CustomHandler)
print("serving at port", PORT)
httpd.serve_forever()
