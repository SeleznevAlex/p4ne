from ipaddress import IPv4Network
import random


class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        ip = random.randint(0x0b000000, 0xdf000000)  # generate ip-borders in int
        mask = random.randint(8, 24)
        IPv4Network.__init__(self, (ip, mask), strict=False)

    def regular(self):
        return self.is_global and not self.is_private

    def __str__(self):
        return "Fresh random network: " + IPv4Network.__str__(self)


netlist = []
while len(netlist) < 5:
    randNet = IPv4RandomNetwork()
    if randNet.regular() and randNet not in netlist:
        netlist.append(randNet)

for net in netlist:
    print(net)
