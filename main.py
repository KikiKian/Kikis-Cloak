import subprocess
import re
import random
import argparse

def genmac():
    parts = []
    for i in range(6):
        newxint = random.randint(0, 255)
        if i == 0:
            newxint = (newxint & 0xfe) | 0x02  
        newxhex = format(newxint, '02x')
        parts.append(newxhex)
    return ':'.join(parts)

def cloak(interface, newmac):
    #ip link set wlp61s0 down
    subprocess.run(["ip", "link", "set", "wlp61s0", "down"])
    #ip link set wlp61s0 address xx:xx:xx:xx:xx:xx
    subprocess.run(["ip", "link", "set", "wlp61s0", "address", newmac])
    #ip link set wlp61s0 up
    subprocess.run(["ip", "link", "set", "wlp61s0", "up"])
    

lines  = subprocess.run(["ip", "link", "show"], capture_output=True, text=True)
macaddresses = [line for line in lines.stdout.splitlines() if "link/ether" in line]

verbosemac = macaddresses[0]
mac = re.search(r'([0-9a-f]{2}:){5}[0-9a-f]{2}', verbosemac)

newmac = genmac()

for line in lines.stdout.splitlines():
    if "state UP" in line:
        interface = line.split(":")[1].strip()
        break

cloak(interface, newmac)

