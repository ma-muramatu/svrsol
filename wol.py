#!/usr/bin/python3
# -*- coding: utf-8 -*-

# pythondialog 3.4.0 documentation
# http://pythondialog.sourceforge.net/doc/index.html

# wakeonlan 1.1.6
# https://pypi.org/project/wakeonlan/

import json
from dialog import Dialog
from wakeonlan import send_magic_packet

file = open('wol.json')
data = json.load(file)
wol = data['Wake On LAN']

items = []
for idx, rec in enumerate(wol):
    items.append(tuple([str(idx), rec["hostname"]]))

d = Dialog(dialog="dialog")

code, tag = d.menu("Wake On LAN", choices=items)
if code=="ok":
    hostname = wol[int(tag)]['hostname']
    mac = wol[int(tag)]['MACaddress']
    print('Send Magic Packet for {}({})'.format(hostname, mac))
    send_magic_packet(mac)

print('Done.')
