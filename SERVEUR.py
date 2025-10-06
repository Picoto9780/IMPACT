import http.server
import socketserver
import mimetypes

PORT = 8000

class BrotliHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Si le fichier se termine par .br, ajoute le header
        if self.path.endswith(".br"):
            self.send_header("Content-Encoding", "br")
            # On peut aussi ajouter le type MIME si nécessaire
            mime_type, _ = mimetypes.guess_type(self.path[:-3])
            if mime_type:
                self.send_header("Content-Type", mime_type)
        super().end_headers()

with socketserver.TCPServer(("", PORT), BrotliHandler) as httpd:
    print(f"Serveur HTTP avec Brotli démarré sur http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServeur arrêté.")
        httpd.server_close()