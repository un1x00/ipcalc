#!/usr/bin/python3


import re
import sys
import ipcalc
from ipcalc import Network

cidr = {
     '0.0.0.0' :  '/0',
    '128.0.0.0' :  '/1',
    '192.0.0.0' :  '/2',
    '224.0.0.0' :  '/3',
    '240.0.0.0' :  '/4',
    '248.0.0.0' :  '/5',
    '252.0.0.0' :  '/6',
    '254.0.0.0' :  '/7',
    '255.0.0.0' :  '/8',
    '255.128.0.0' :  '/9',
    '255.192.0.0' :  '/10',
    '255.224.0.0' :  '/11',
    '255.240.0.0' :  '/12',
    '255.248.0.0' :  '/13',
    '255.252.0.0' :  '/14',
    '255.254.0.0' :  '/15',
    '255.255.0.0' :  '/16',
    '255.255.128.0' :  '/17',
    '255.255.192.0' :  '/18',
    '255.255.224.0' :  '/19',
    '255.255.240.0' :  '/20',
    '255.255.248.0' :  '/21',
    '255.255.252.0' :  '/22',
    '255.255.254.0' :  '/23',
    '255.255.255.0' :  '/24',
    '255.255.255.128' :  '/25',
    '255.255.255.192' :  '/26',
    '255.255.255.224' :  '/27',
    '255.255.255.240' :  '/28',
    '255.255.255.248' :  '/29',
    '255.255.255.252' :  '/30',
    '255.255.255.254' :  '/31',
    '255.255.255.255' :  '/32'
}

def usage():
    print ("""
    usage: inet [ip] [mask] [option] ... [ n network | b broadcast | c compare | d destination | r range ]
    option and arguments:
    n         network            : displays the network address
    b         broadcast          : displays the broadcast address
    c         compare            : compares two address and masks to see if in the same network
    d         destination        : displays the other end of a /30 address (only use with /30)
    r         range              : displays all addresses in the network
    m         mask               : converts masks from /30 (cidr) to full, or vice versa

   examples:
    [*]         inet 10.10.10.2 255.255.255.252 n       - displays the network address of 10.0.0.0
    [*]         inet 10.10.10.2 /30 b                   - displays the broadcast address of 10.10.10.3
    [*]         inet 10.10.10.2 /23 c 10.10.10.7 /23    - displays as True as both are in the same network
    [*]         inet 192.168.1.1 /22 m                  - displays 192.168.1.1 255.255.252.0""")


def network():
    if re.match('\d+\.\d+\.\d+\.\d+', sys.argv[2]):
        ip = sys.argv[1]
        subnet = ipcalc.Network(ip + cidr.get(sys.argv[2]))
        print (str(subnet.network()))
        exit(0)
    elif re.match('\/\d+', sys.argv[2]):
        ip = sys.argv[1]
        subnet = ipcalc.Network(ip + sys.argv[2])
        print (str(subnet.network()))
        exit(0)
def range():
    if re.match('\d+\.\d+\.\d+\.\d+', sys.argv[2]):
        ip = sys.argv[1]
        subnet = ipcalc.Network(ip + cidr.get(sys.argv[2]))
        for x in ipcalc.Network(subnet):
            print (str(x))
        exit(0)
    elif re.match('\/\d+', sys.argv[2]):
        ip = sys.argv[1]
        subnet = ipcalc.Network(ip + sys.argv[2])
        for x in ipcalc.Network(subnet):
            print (str(x))
        exit(0)
def destination():
    if re.match('\d+\.\d+\.\d+\.252', sys.argv[2]):
        ip = sys.argv[1]
        subnet = ipcalc.Network(ip + cidr.get(sys.argv[2]))
        for x in ipcalc.Network(subnet):
            if str(x) != str(ip):
                print (str(x))
        exit(0)
    elif re.match('\/30', sys.argv[2]):
        ip = sys.argv[1]
        subnet = ipcalc.Network(ip + sys.argv[2])
        for x in ipcalc.Network(subnet):
            if str(x) != str(ip):
                print (str(x))
        exit(0)
    else:
        print('Sorry, only /30 for destination')
        exit(0)
def broadcast():
    if re.match('\d+\.\d+\.\d+\.\d+', sys.argv[2]):
        ip = sys.argv[1]
        subnet = ipcalc.Network(ip + cidr.get(sys.argv[2]))
        print (str(subnet.broadcast()))

    elif re.match('\/\d+', sys.argv[2]):
        ip = sys.argv[1]
        subnet = ipcalc.Network(ip + sys.argv[2])
        print (str(subnet.broadcast()))
        exit(0)
def mask():
    try:
        if re.match('\d+\.\d+\.\d+\.\d+', sys.argv[2]):
            ip = sys.argv[1]
            subnet = sys.argv[2]
            subnet = cidr.get(subnet)
            print(ip + subnet)
        elif re.match('\/\d+', sys.argv[2]):
            ip = sys.argv[1]
            subnet = sys.argv[2]
            for item in cidr.items():
                if subnet in item:
                    print(ip, item[0])
    except:
        print('I suspect the subnet mask is invalid')
    exit(0)

def compare():    if re.match('\d+\.\d+\.\d+\.\d+', sys.argv[2]):
        ip = sys.argv[1]
        ip2 = sys.argv[4]
        subnet = ipcalc.Network(ip + cidr.get(sys.argv[2]))
        subnet2 = ipcalc.Network(ip2 + cidr.get(sys.argv[5]))
        network = str(subnet.network())
        network2 = str(subnet2.network())
        if network == network2:
            print ('True')
            exit(0)
        else:            print ('False')
            exit(0)
    elif re.match('\/\d+', sys.argv[2]):
        ip = sys.argv[1]
        ip2 = sys.argv[4]
        subnet = ipcalc.Network(ip + sys.argv[2])
        subnet2 = ipcalc.Network(ip2 + sys.argv[5])
        network = str(subnet.network())
        network2 = str(subnet2.network())        if network == network2:
            print ('True')            exit(0)
        else:            print ('False')
            exit(0)
    elif re.match('\/\d+', sys.argv[2]):
        ip = sys.argv[1]
        subnet = ipcalc.Network(ip + sys.argv[2])
        print (str(subnet.broadcast()))
        exit(0)
    elif re.match('\/\d+', sys.argv[2]):
        ip = sys.argv[1]        subnet = ipcalc.Network(ip + sys.argv[2])
        print (str(subnet.broadcast()))
        exit(0)
def main():
    if re.match('\d+\.\d+\.\d+\.\d+\/\d+', sys.argv[1]):
        inet = sys.argv[1].split('/')
        sys.argv.append(sys.argv[2])
        sys.argv[1] = inet[0]
        sys.argv[2] = "/" + inet[1]

    if sys.argv[3] == str('n'):
        network()
    if sys.argv[3] == str('r'):
        range()
    if sys.argv[3] == str('d'):
        destination()
    if sys.argv[3] == str('b'):
        broadcast()
    if sys.argv[3] == str('m'):
        mask()
    if sys.argv[3] == str('c'):
        compare()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print (usage())
        exit(1)
    elif sys.argv[2] == str('c'):
        if re.match('\d+\.\d+\.\d+\.\d+\/\d+', sys.argv[1]):
            inet = sys.argv[1].split('/')
            sys.argv.append(sys.argv[2])
            sys.argv[1] = inet[0]
            sys.argv[2] = "/" + inet[1]
            inet = sys.argv[3].split('/')
            sys.argv.append(sys.argv[4])
            sys.argv[3] = inet[0]
            sys.argv[4] = "/" + inet[1]
            ip = sys.argv[1]
            ip2 = sys.argv[3]
            subnet = ipcalc.Network(ip + sys.argv[2])
            subnet2 = ipcalc.Network(ip2 + sys.argv[4])
            network = str(subnet.network())
            network2 = str(subnet2.network())
            if network == network2:
                print ('True')
                exit(0)
            else:
                print ('False')
                exit(0)
    else:
        main()
        exit(0)
