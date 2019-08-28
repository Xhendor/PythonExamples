from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO
from urllib.parse import urlparse
import simplejson

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        query = urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        imsi = query_components["edad"]
        if int(imsi) < 18:
          self.wfile.write(b'<div style=\'color: blue;\'>So sorry, tas chavo!!</div>')
        else:
          self.wfile.write(b'<b>Hello, world!</b>')
          self.wfile.write(str.encode('\n'+imsi))



    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        data = simplejson.loads(body)
        response.write(str.encode('<br><b>calle: '+data['street']+'</b><br>'))
        response.write(str.encode('<b>Codigo Postal: '+data['zipcode']+'</b><br>'))
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
