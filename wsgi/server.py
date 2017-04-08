from wsgiref.simple_server import make_server
from wsgi import application

httpd = make_server('', 8080, application)
print('server started on port 8080')

httpd.serve_forever()
