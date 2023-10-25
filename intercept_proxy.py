import custom_proxy
import sys

server = custom_proxy.TheServer('localhost', 12345)
try:
    server.main_loop()
except KeyboardInterrupt:
    print("Ctrl C - Stopping server")
    sys.exit(1)