import random

"""
This RSA library provides functions to generate, encrypt and decrypt integers bigger than 2 with RSA cryptation.
RSA cryptation is a public-key cryptosystem that is widely used for secure data transmission.

The key size is by default 1024 bits. This can changed in the _prime() functions. (The key size is n * 2.)

RSA cryptation is essentially two key pairs, one public and private pair. 
Anyone can use the public key to decrypt a message, but can only be decoded the private key pair.

Usage example:
Alice generates a public & private key pair and makes the public key pair public. 
Bob uses the public key pair to encrypt a message, and sends this encrypted message to Alice.
Alice uses the private key pair to decrypt Bob's message. 

Library usage example:
> keys = generate()
keys[0] is the public and keys[1] is the private key pair. 
> encrypted_message = encrypt(keys[0], 299792458)
Returns the encryption of 299792458.
> message = decrypt(keys[1], encrypted_message)
Returns the message 299792458.

encryptation/decryptation uses Fast Modular Exponentiation for Time efficiency.
For safely reasons, large random prime numbers is used. (512-bit by default.) 
For efficent calculation of big primes, a weak primalitytest is first used. 
If passed, the number goes through Miller-Rabin primality test 20 times by default. Can be changed _MRTest. (The bigger the better)
The Miller-Rabin test is a probabilistic primality test: an algorithm which determines whether a given number is likely to be prime.
If a number passes the test, it's probability of not to being a prime is 1/4. Thus, the probability of a number passing the weak
test and Miller-Rabin 20 times and NOT being a prime is in the order of ~ 4**(-20). 
"""

def encrypt(public_key,x):
    """Returns encrypted message based on a public_key pair.

        input: public_key pair, integer x to be encrypted.
        output: integer z as integer x encrypted.
        """
    return _mod_exp(public_key,x)

def generate():
    """Returns a public_key pair and corresponding private_key pair.

        output: [public_key, private_key]
        """
    p1 = _prime()
    p2 = _prime()
    public_key = [p1*p2, 2**64 + 1]
    private_key = [public_key[0], _EuclidianAlgorithm(public_key[1],(p1-1)*(p2-1))]
    print('Public key:', public_key)
    print('Private key:', private_key)
    return [public_key, private_key]


def decrypt(private_key,x):
    """Returns decrypted message.

        input: Private key pair, encrypted message x.
        output: Decypted message x.
    """
    return _mod_exp(private_key,x)

def _EuclidianAlgorithm(a,n):
    t = 0
    r = n
    newt = 1
    newr = a
    while newr != 0:
        quotient = r // newr
        [t,newt] = [newt, t - quotient * newt]
        [r,newr] = [newr, r - quotient * newr]
    if r > 1:
        return None
    if t < 0:
        t = t + n
    return t

def _mod_exp(key_pair,b):
    # Computes b ** key_pair[1] % key_pair[0]
    pc = list(key_pair)
    while b < 0:
        b += pc[0]

    r = 1
    if 1 & pc[1]:
        r = b
    while pc[1]:
        pc[1] >>= 1
        b = (b * b) % pc[0]
        if pc[1] & 1: r = (r * b) % pc[0]

    return r


def _randint(n):
    return random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)


def _PossiblePrime(n):
    # Weak primalitytest
    first_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                         31, 37, 41, 43, 47, 53, 59, 61, 67,
                         71, 73, 79, 83, 89, 97, 101, 103,
                         107, 109, 113, 127, 131, 137, 139,
                         149, 151, 157, 163, 167, 173, 179,
                         181, 191, 193, 197, 199, 211, 223,
                         227, 229, 233, 239, 241, 251, 257,
                         263, 269, 271, 277, 281, 283, 293,
                         307, 311, 313, 317, 331, 337, 347, 349]
    while True:
        pc = _randint(n)
        for divisor in first_primes:
            if pc % divisor == 0 and divisor ** 2 <= pc:
                break
        else:
            return pc


def _MRTest(mrc):
    # Miller-Rabin primality test
    mDBT = 0
    ec = mrc - 1
    while ec % 2 == 0:
        ec >>= 1
        mDBT += 1
    assert (2 ** mDBT * ec == mrc - 1)

    def _TC(rt):
        if pow(rt, ec, mrc) == 1:
            return False
        for i in range(mDBT):
            if pow(rt, 2 ** i * ec, mrc) == mrc - 1:
                return False
        return True

    MRTrials = 20 # No. of Miller-Rabin trials
    for i in range(MRTrials):
        rt = random.randrange(2, mrc)
        if _TC(rt):
            return False
    return True


def _prime():
    while True:
        n = 512 # Bit length of prime.
        prime_candidate = _PossiblePrime(n)
        if not _MRTest(prime_candidate):
            continue
        else:
            return prime_candidate


