"""
 Implements a simple HTTP/1.0 Server

"""

import socket

# def renderTemplate(path):
#     if path == '/':
#         #templates = 'templates/index.html'
#         fin = open('templates/index.html').read()
#     elif path == '/about':
#         templates = 'templates/about.html'
#     else:
#         content = "error"

    #fin = open(templates).read()
    #content = fin.read()
    #fin.close()

# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print("Server started http://%s:%s" % (SERVER_HOST, SERVER_PORT))

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode().split(' ')
    path = request[1]
    #print(f' requested Full stack : {request}')
    request = request[-6].split("\n")[0].split("/")
    #print(f' requested Split : {request}')
    request = request[-1]
    #print(f' requested Split : {request}')
    if request != 'document\r':
        if request.split("?") != ['\r']:
            request = request.split("?")[-1].split("&")
            fname = request[0].split("=")[-1]
            fpass = request[1].split("=")[-1]

            print(f'fname : {fname}')
            print(f'fpass : {fpass}')

    print(f'path : {path}')
    if path.endswith('/'):
        path =path[:-1]

    if path == '':
        #templates = 'templates/index.html'
        content = open('template/register.html').read()
    elif path == '/register':
        content = open('template/register.html').read()


    # Send HTTP response
    response = f'HTTP/1.0 200 OK\n\n'+content
    client_connection.sendall(response.encode())
    client_connection.close()
# Close socket
server_socket.close()