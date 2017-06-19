from http.server import BaseHTTPRequestHandler,HTTPServer
import http
from unread_email import unread_email_count
import codecs
import ipaddress
import urllib
from urllib.parse import urlparse,parse_qs
HOST_NAME = 'localhost'
PORT_NUMBER = 8080
class myHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            p1 = urlparse(self.path)
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            if(p1.query != ''):
                p2 = parse_qs(p1.query)
                k = unread_email_count(str(p2['login'][0]),str(p2['pwd'][0]))
                send = codecs.encode(str(k))
                self.wfile.write(send)
            else:
                self.wfile.write(b'NULL')
        except ValueError:
            self.wfile.write(b'NULL')
        except Exception as e:
            self.wfile.write(b'NULL')            
        return
try:
    HOST_NAME = input('please input HOST_NAME: ')
    if HOST_NAME != 'localhost':
        try:
            ipaddress.ip_address(HOST_NAME)
        except ValueError:
            HOST_NAME = 'localhost'
            print('false value for HOST_NAME, use "localhost"')
    try:
        PORT_NUMBER = input('please input PORT_NUMBER: ')
        if(int(PORT_NUMBER) > 65535 or int(PORT_NUMBER)<0):
            print('false value for PORT_NUMBER, use "8080"')
            PORT_NUMBER = 8080
    except ValueError:
        print('false value for PORT_NUMBER, use "8080"')
        PORT_NUMBER = 8080
    server = http.server.HTTPServer((HOST_NAME, int(PORT_NUMBER)), myHandler)
    print ('Started httpserver on port ', PORT_NUMBER)
    server.serve_forever()
except KeyboardInterrupt:
    print ('^C received, shutting down the web server')
    server.socket.close()

