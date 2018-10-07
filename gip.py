#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ipgetter
# https://github.com/phoemur/ipgetter

# pythondialog 3.4.0 documentation
# http://pythondialog.sourceforge.net/doc/index.html

import ipgetter
from dialog import Dialog

MyIPaddress = ipgetter.myip()

d = Dialog(dialog="dialog")

code, tag = d.msgbox("Global IP Address is " + MyIPaddress)

print('Done.')
