import sys
from transceiver import *

MY_HOST= '127.0.0.1'
MY_PORT= sys.argv[1]
MY_PORT = int(MY_PORT)

receiver(MY_HOST,MY_PORT)