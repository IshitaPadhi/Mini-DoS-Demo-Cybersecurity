"""
=========================================================
Mini DoS Lab

server.py

Acts as the victim server.

Author : Ishita Padhi
=========================================================
"""

# Import HTTP server
from http.server import HTTPServer, BaseHTTPRequestHandler

# Counter for requests
request_count = 0


# Create custom handler
class MyServer(BaseHTTPRequestHandler):

    # This function runs whenever someone visits the server
    def do_GET(self):

        global request_count

        # Increase request counter
        request_count += 1

        # Print request count
        print(f"Requests Received : {request_count}")

        # Send success response
        self.send_response(200)

        self.end_headers()

        # Send message back
        self.wfile.write(b"Hello from Mini DoS Lab")


# Start server
server = HTTPServer(

    ("localhost", 8000),

    MyServer

)

print("=" * 50)
print("Victim Server Running")
print("URL : http://localhost:8000")
print("=" * 50)

# Keep server running forever
server.serve_forever()