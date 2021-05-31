# RSA encryption


### Description

RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is used for secure data transmission. 
An RSA user has a public key (2048 to 4096 bit is typical) based on two large prime numbers, which are kept secret. 
Anyone can use the public key to decrypt a message, but can only be decoded by those who knows the prime numbers.
This library uses the Miller-Rabin primality test to generate random prime numbers efficently with an error order of <i> ~ 4<sup>-20</sup> </i>.  

### Usage of this library

* Encrypt()

Generates encrypted message based on given public key pair. 

* Generate()

Generate a public and private key pair.

* Decrypt()

Decrypts a message using a private key pair.


### Library usage example

```> keys = generate()```

keys[0] is the public and keys[1] is the private key pair. 

```> encrypted_message = encrypt(keys[0], 299792458)```

Returns the encryption of 299792458.

```> message = decrypt(keys[1], encrypted_message) ```

Returns the message 299792458.

### For in-depth information:

[RSA wiki](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

[Miller–Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)

### Roadmap

* This API is frozen.

*Any documentation or implementation improvments may be pushed. New features may be added.*

Oskar Mevik Päts - [mevikpats](https://github.com/mevikpats)
