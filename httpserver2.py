from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import mimetypes

host = '127.0.0.1'
port = 7787

class NeuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        # Get requested path
        filepath = self.path.strip("/")
        if filepath == "":
            filepath = "index.html"   # default file

        # Check if file exists
        if os.path.exists(filepath) and os.path.isfile(filepath):
            # Guess MIME type (html, css, js, jpg, png, etc.)
            mimetype, _ = mimetypes.guess_type(filepath)
            if mimetype is None:
                mimetype = "application/octet-stream"

            # Send response headers
            self.send_response(200)
            self.send_header("Content-type", mimetype)
            self.end_headers()

            # Read and send file
            with open(filepath, "rb") as f:
                self.wfile.write(f.read())
        else:
            # File not found → 404 error
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>404 File Not Found</h1>")

server = HTTPServer((host, port), NeuralHTTP)

print("[+] Server has been Started ....")
print('[+] Using This Link ', f'http://{host}:{port}')

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass

server.server_close()
print("[-] Server Stopped...")
