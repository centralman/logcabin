from filters.json import Json
from filters.mutate import Mutate
from filters.regex import Regex
from flow import Fanin, Fanout, If, Switch
from inputs.zeromq import Zeromq
from outputs.log import Log

with Fanin():
    Zeromq(address='tcp://*')

with Switch() as case:
    with case(lambda ev: ev.field == 'value'):
        Json()
    with case.default:
        Regex(regex='abc')

with If('a==1'):
    Mutate()

with Fanout():
    Log()
