from RPFirmware.GPS import GPS


g = GPS()
print(g.getTpsLatLonAlt(prec=15))

