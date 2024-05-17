from pox.core import core
from pox.lib.util import dpid_to_str
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class MyComponent (object):
    def __init__(self):
        core.openflow.addListeners(self)
        self.mac_to_port = {}

    def _handle_ConnectionUp(self, event):
        self.connection = event.connection
        log.debug("Switch %s has come up.", dpid_to_str(event.dpid))

    def _handle_PacketIn(self, event):

        packet = event.parsed # This is the parsed packet data.
        if not packet.parsed:

            log.warning("Ignoring incomplete packet")
            return

        packet_in = event.ofp # The actual ofp_packet_in message.

        msg = of.ofp_packet_out()
        msg.data = packet_in
        print("Received packet from port %d" % packet_in.in_port)

        
def launch():
        core.registerNew(MyComponent)

