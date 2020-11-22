#!/usr/bin/env python
cipher=[70, 108, 97, 103, 123, 67, 67, 83, 67, 95, 99, 114, 121, 112, 116, 111, 125]
flag=""
for x in cipher:
	flag+=chr(x)
print(flag)
