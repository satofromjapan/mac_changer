#!/user/bin/env python

import subprocess
import optparse
from re import search
from random import randint


def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address, you can also use 'random' to generate a random MAC Address")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")

    if not options.new_mac:
        parser.error("[-] Please specify a new MAC, use --help for more info.")

    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC Address for {0} to {1}".format(interface, new_mac))

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_output = subprocess.check_output(["ifconfig", interface])
    ifconfig_results = search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_output.decode("utf-8"))

    if ifconfig_results:
        return ifconfig_results.group(0)
    else:
        print("[-] Could not read MAC address")

def randomMAC():
    generated_mac = [0x00, 0x16, 0x3e, randint(0x00, 0x7f), randint(0x00, 0xff), randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, generated_mac))

options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC = {0}".format(current_mac))

if options.new_mac == 'random':
    altered_mac = randomMAC()
    change_mac(options.interface, altered_mac)
else:
    altered_mac = options.new_mac
    change_mac(options.interface, altered_mac)

current_mac = get_current_mac(options.interface)

if current_mac == altered_mac:
    print("[+] MAC address was successfully changed to {0}".format(current_mac))
else:
    print("[-] MAC address did not get changed.")
