"""
    RSA Encryption
    1. find two large prime number p, q
    2. let N = p * q
    3. r = (p-1) * (q-1)
    4. find a number e that is smaller than r and co-prime with r
    5. ed = 1 mod r
    6. (N, e) are public key
    7. d is private key

    Encryption:
    1. Given a plain text M
    2. Transfer M into number form m
    3. C = m^e mod N
    4. C is cipher text

    Decryption:
    1. m = C^d mod N
    2. Transfer m into plain text M
"""

def find_coprime(r):
    e = 0
    for i in range(1, r):
        if r % i != 0:
            return i

def find_module(r, e):
    emu = 0
    while True:
        if (e * emu) % r == 1:
            return emu
        else:
            emu += 1

# step 1
p = int(raw_input("Please type a prime number: "))
q = int(raw_input("Please type another prime number: "))
# step 2
N = p*q
# step 3
r = (p-1)*(q-1)
# step 4
e = find_coprime(r)
# step 5
d = find_module(r, e)
print("p: %d q: %d N: %d r:%d e:%d d:%d" % (p, q, N, r, e, d))
print("Public Key: (%d, %d); Private Key: %d" % (N, e, d))

def encryption(m):
    return m ** e % N

def decryption(c):
    return c ** d % N

m = int(raw_input("Please input number text m: "))

c = encryption(m)
print("cipher text: %d" % c)
print("plain text: %d" % decryption(c))

