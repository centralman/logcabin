from filters.json import Json
from flow import Fanin, Fanout
from inputs.zeromq import Zeromq
from outputs.log import Log

with Fanin():
    Zeromq(address='tcp://*')

Json()

with Fanout():
    Log()
