#!/usr/bin/env python
cipher=" ,=$1\"'6/\"'*,- c,-s:,6!c%*!07c+,1c0+\"/?"
key="CCSC"
flag=""
i=0
for x in cipher:
	flag+=chr(ord(x)^(ord(key[i%len(key)])))
	i+=1
print(flag)
