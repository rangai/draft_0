import sys
from transceiver import Transceiver

MY_PORT= sys.argv[1]
MY_PORT = int(MY_PORT)

r = Transceiver()
r.receive(MY_PORT)