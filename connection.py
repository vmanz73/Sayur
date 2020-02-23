import urllib.request
def connect(host='http://http://128.1.2.1'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
# test
print( 'connected' if connect() else 'no internet!' )