# import the inputs and an output
from filters.json import Json
from inputs.udp import Udp
from outputs.file import File

Udp(port=6000)
# parse the event as json
Json()
# log the results to output.log
File('output.log')
