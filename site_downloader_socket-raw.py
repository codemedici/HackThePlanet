import sys, socket

try:
    host = str(sys.argv[1])
except (IndexError, ValueError):
    print('Must supply url')
    sys.exit(2)

port = 80
sock = socket.create_connection((host, port))

req = (
    'GET HTTP/1.0\r\n'
    'Host: {host}:{port}\r\n'
    'User-Agent: Python {version}\r\n'
    'Connection: close\r\n'
    '\r\n'
)
req = req.format(
    host=host,
    port=port,
    version=sys.version_info[0]
)
sock.sendall(req.encode('ascii'))
rfc_raw = bytearray()
while True:
    buf = sock.recv(4096)
    if not len(buf):
        break
    rfc_raw += buf
rfc = rfc_raw.decode('utf-8')
print(rfc)

