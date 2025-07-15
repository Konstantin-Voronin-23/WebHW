from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """Метод для обработки GET-запросов"""
        try:
            with open("./html/contacts_pg.html", "r", encoding="utf-8") as file:
                html_content = file.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(bytes(html_content, "utf-8"))

        except FileNotFoundError:

            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>404 - Page Not Found</h1>")

if __name__ == "__main__":
    """Запуск"""
    web = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started at http://{hostName}:{serverPort}")

    try:
        web.serve_forever()
    except KeyboardInterrupt:
        pass

    # Остановка сервера
    web.server_close()
    print("Server stopped.")