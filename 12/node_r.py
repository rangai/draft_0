import sys
from transceiver import *

MY_PORT= sys.argv[1]
MY_PORT = int(MY_PORT)

receive(MY_PORT)