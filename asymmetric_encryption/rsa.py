
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def encrypt(message, n, c):
    message_letters = [ord(letter) for letter in message]
    message_encrypted = ''.join([chr(letter**c % n) for letter in message_letters])
    return message_encrypted


def decrypt(message_encrypted, n, d):
    message_encrypted_letters = [ord(letter) for letter in message_encrypted]
    message = ''.join([chr(letter**d % n) for letter in message_encrypted_letters])
    return message

def keygen(p1, p2):
    n = p1 * p2
    
    totient = (p1 - 1) * (p2 - 1)

    public_keys = []
    for i in range(totient):
        if gcd(i, totient) == 1:
            public_keys.append(i)

    # selecting just the 5th one as public key, any could be selected
    public_key = public_keys[4]

    private_key = 0
    x = -1
    while x != 0:
        private_key += 1
        x = (public_key * private_key - 1) % totient

    return (n, public_key, private_key)

p1 = 13
p2 = 17
msg = 'jyapu shakya'


n,c,d = keygen(p1,p2)

print('n, c, d is ', n,c,d)
enc = encrypt(msg, n, c)
print('encrypted form is {}'.format(enc))
dec = decrypt(enc, n, d)
print('decrypted form is {}'.format(dec))