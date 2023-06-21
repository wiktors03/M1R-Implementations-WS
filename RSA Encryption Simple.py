from math import gcd
import random 

#we select two prime numbers, for maximum security these should be large, but for the example we will use two standard primes. 

p = 3
q = 7
n = p*q 

#we then compute phi(n), which is as follows

phi_n = (p-1)*(q-1)

#we then select a integer e with the proprties descirbed earlier throughout the poster.

e = 2
for i in range(2, phi_n):
  if gcd(i, phi_n) == 1:
    e = i
    break




#we then find the value d, the modulo inverse

d = pow(e,-1,phi_n)



#the encryption algorithm can be done as follows:
message = 18
ciphertext = (message ** e) % n
print(f"Encrypted message is {ciphertext}")

    # performing decryption
message_decrypt = (ciphertext ** d) % n
print(f"Decrypted message is {message_decrypt}")
