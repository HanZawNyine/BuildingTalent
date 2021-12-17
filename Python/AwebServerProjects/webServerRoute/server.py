from http.server import HTTPServer, BaseHTTPRequestHandler


class helloHandller(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        if self.path == '/':
            self.render(self.path, "/templates/index.html"),
        elif self.path == '/second':
            self.render(self.path, '/templates/second.html')

    def render(self, path='/', template='/templates/index.html'):
        template = template[1:]
        print("templates : ", template)
        htmlStr = ''
        try:
            htmlStr = open(template).read()
            print("___", htmlStr)
            self.send_response(200)
        except:
            htmlStr = f"{self.path}{template} is not found"
            print(htmlStr)
            self.send_response(404)

        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(htmlStr.encode())


if __name__ == '__main__':
    port = 8000
    servername = 'localhost'
    server = HTTPServer((servername, port), helloHandller)
    print("Server started http://%s:%s" % (servername, port))
    server.serve_forever()
