#!/usr/bin/python3
"""a simple web server"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SamServer(BaseHTTPRequestHandler):

    def do_GET(self):
        response = json.dumps({"name": "John", "age": 30, "city": "New York"})

        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(response.encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.end_headers()

        elif self.path == '/':
            self.send_response(200, "Hello, this is a simple API!")
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        else:
            self.send_response(404, "page does not exist")
            self.end_headers()


server = HTTPServer(('', 8000), SamServer)
server.serve_forever()
server.server_close()
