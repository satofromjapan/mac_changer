# Mac Changer (placeholder name)

A hobby Mac Changer program to change your mac address of any network interface, to any MAC Address

## Basic Usage

Run the file using python3 and add the flags.

Example
```
python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

## Flags

#### Interface
Use the `-i` or `--interface` flag to specify the interface

#### MAC Address
Use the `-m` or `--mac` followed by the MAC Address you want to change to. You can also enter `random` to generate a random MAC Address

## Features to come
- [x] Random MAC Address
- [ ] Others as I think of them...
