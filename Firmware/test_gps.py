from RPFirmware.resources.GPS import GPS


g = GPS()
print(g.getTpsLatLonAlt(prec=15))

