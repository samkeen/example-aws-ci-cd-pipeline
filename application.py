from wsgiref.simple_server import make_server

response = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AWS CI/CD Demo</title>
</head>
<body>
<h1>AWS CI/CD Demo</h1>
</body>
</html>
"""

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [response]


if __name__ == '__main__':
    httpd = make_server('', 8999, application)
    print("Serving on port 8999...")
    httpd.serve_forever()
