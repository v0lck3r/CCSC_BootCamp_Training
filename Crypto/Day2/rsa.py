#!/usr/bin/env python


from Crypto.Util.number import inverse,long_to_bytes


# given : 

n=882564595536224140639625987659416029426239230804614613279163
c=348226401953293105681528097015649924012602919180196628514181
e=65537

#try to factorise it w/ : factordb.com or https://www.alpertron.com.ar/ECM.HTM to get p and q 

q = 857504083339712752489993810777
p = 1029224947942998075080348647219

# phi : 

phi = ( p -1 )*( q - 1 )
d = inverse(e, phi)

m = pow(c, d, n)

print hex(m)[2:-1].decode('hex')

#print long_to_bytes(m)
