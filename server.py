#!/usr/bin/env python3
"""Simple HTTP server that returns 'hello world!' when accessed."""

from http.server import HTTPServer, BaseHTTPRequestHandler


class HelloWorldHandler(BaseHTTPRequestHandler):
    """Handler that responds with 'hello world!' to all requests."""

    def do_GET(self):
        """Handle GET requests."""
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"hello world!")

    def do_HEAD(self):
        """Handle HEAD requests."""
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()


def main():
    """Start the HTTP server."""
    host = "0.0.0.0"  # Listen on all interfaces for internet access
    port = 8080

    server = HTTPServer((host, port), HelloWorldHandler)
    print(f"Server running on http://{host}:{port}")
    print("Press Ctrl+C to stop")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.shutdown()


if __name__ == "__main__":
    main()
