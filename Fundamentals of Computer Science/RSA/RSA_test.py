import RSA as rsa

def main():
    keys = rsa.generate()

    for x in [2, rsa._prime(), rsa._prime() + 1]: # [0] base case, [1] random 512-bit prime, [2] random 512-bit nonprime.
        y = rsa.encrypt(keys[0],x)
        assert(x != y)
        z = rsa.decrypt(keys[1],y)
        assert(z == x) #Asserts that all functions in RSA is working.

if __name__ == "__main__":
    main()
