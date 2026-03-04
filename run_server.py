# preview_site.py
import http.server
import socketserver
import webbrowser

PORT = 8000

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    webbrowser.open(f"http://localhost:{PORT}/index.html")
    print(f"Serving at http://localhost:{PORT}/index.html")
    httpd.serve_forever()
