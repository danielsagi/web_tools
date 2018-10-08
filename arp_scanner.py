import sys
import requests 
from scapy.all import ARP, Ether, conf, srp

conf.verb = 0

w = '\033[37m' 
g = '\033[32m' 
b = '\033[34m' 
y = '\033[33m' 
c = '\033[36m' 

def show_identity(pkt):
    metadata = requests.get('http://macvendors.co/api/{}'.format(pkt[Ether].src)).json()['result']
    print w+"{mac} - {ip} ({company})".format(mac=pkt[Ether].src, ip=ans[ARP].psrc, company=metadata['company'])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        cidr = sys.argv[1]
    else:
        cidr = raw_input("please enter a CIDR: ")

    print c+"[*] scanning..."
    answers, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = cidr), timeout = 2, inter = 0.1)

    print g+"[*] scan completed"+w+"\n\nDevices on network"
    for _, ans in answers:
        show_identity(ans)