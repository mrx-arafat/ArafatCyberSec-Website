import http.server
import socketserver

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print("Headers: ", self.headers)
        print("Body: ", post_data.decode('utf-8'))

        # Respond with a 200 status code
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Received')

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
