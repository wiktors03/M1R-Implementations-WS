import ecdsa
import random
import libnum
import hashlib
import sys
#these are some of the basic standard python encryption tool libraries we can use

G = ecdsa.SECP256k1.generator
#we select the private curve, in this case we have chosen SECP256k1 a common curve

order = G.order()
#we require the order of G, a point that nG=0 (where 0 is the identity)

priv_key= random.randrange(1,order)
#we generate the private key, a randomly selected numberbetween 1 and the order.abs

pub_key = ecdsa.ecdsa.Public_key(G, G*priv_key)
#we generate the public key using the inbuilt functions

d = ecdsa.ecdsa.Private_key(pub_key, priv_key)
k = random.randrange(1, 2**127)
#this is a cryptographically secure number chosen for the process

msg = "Recoveryattack"

if (len(sys.argv)>1):
	msg=(sys.argv[1])

h = int(hashlib.sha256(msg.encode()).hexdigest(),base=16)
#it is worth noting here that tot perform this attack, the attack must know the hash(sha256) beforehand

sig = d.sign(h, k)
r,s = sig.r,sig.s

#and now using these values of r and s, we generate a fualt.

rf = sig.r+1
sf=(libnum.invmod(k,order)*(h+priv_key*rf)) % order

k = h*(s-sf) * libnum.invmod(sf*r-s*rf,order)
valinv = libnum.invmod( (sf*r-s*rf),order)
recovered_key =(h*(s-sf)* valinv) % order

#this is the attack we used in the poster, using the same strategy as before. 
print(priv_key)
print(recovered_key)
print(priv_key==recovered_key)
