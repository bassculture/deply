import deply as deply

def Site():
    return deply.Site(host = 'example.com', port = 22)

def Puts():
    result = [
        deply.Target('/local/path/foo/bar', '/www/foo/bar', 0755),
    ]
    return result

