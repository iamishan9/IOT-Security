# importing all libraries
from asymmetric_encryption import goldwasser,elgamal,rsa,rsa_image
import random
from asymmetric_encryption.rsa_audio import rsa_audio_enc_dec
from prime_gen_test import eratosthenes,miller_rabin
from utils import bcolors

# test function for goldwasser
def check_goldwasser():

    # generating prime numbers 
    prime_numbers = eratosthenes.gen_prime(500)
    p, q = 0, 0
    p_done = False
    q_done = False

    # checking for conditions
    for i in reversed(prime_numbers):
        if not miller_rabin.millerRabin(i):
            if not(p_done):
                if i%4==3:
                    p=i
                    p_done= True
            else:
                if i%4==3:
                    q=i
                    break
    bits=10
    # message to be encrypted
    msg='Hello, we are testing Blum Goldwasser encryption'

    # converting message to bits
    m=goldwasser.to_bits(msg)
    a=1
    b=1

    # getting a and b
    _,a,b=goldwasser.xgcd(p,q)

    # getting random number
    r= random.getrandbits(bits)
    x0 = (a*p*r + b*q+r) % (p*q)
    n = p * q
    c, xt = goldwasser.BGW_enc(n , x0, m)

    # printing the parameters
    print(bcolors.OKGREEN+"\nBLUM GOLDWASSER",bcolors.ENDC)
    print(bcolors.OKBLUE+"\nParameters chosen:",bcolors.ENDC)
    print(("p= %d" % p))
    print(("q= %d" % q))
    print(("a= %d" % a))
    print(("b= %d" % b))
    print(("r= %d" % r))
    print(("x0= %d" % x0))
    print(("ap+bq: %d" % (a*p+b*q)))

    # printing ciphertext and decrypted message
    print(bcolors.OKBLUE+"\nCiphertext:",bcolors.ENDC, c)
    d = goldwasser.BGW_dec(p, q, a, b, xt, c)
    print(bcolors.OKBLUE+"Decrypted message:",bcolors.ENDC ,goldwasser.from_bits(d))


# test function for elgamal
def check_el_gamal():

    print(bcolors.OKGREEN+"\nEL GAMAL\n",bcolors.ENDC)

    # printing kets
    print(bcolors.OKBLUE+"Generating keys first:",bcolors.ENDC)
    keys = elgamal.generate_keys()
    priv = keys['privateKey']
    pub = keys['publicKey']
    print("p:", pub.p)
    print("g:", pub.g)
    print("A:", pub.A)

    # message for encyption
    message = 'We are testing El Gamal'
    cipher = elgamal.digit(pub, str(message))

    # printing cipher and decypted message
    decrypted_message = elgamal.decipher(priv, pub, cipher)
    print(bcolors.OKBLUE+"The cipher is: ",bcolors.ENDC, cipher)
    print(bcolors.OKBLUE+"Decrypted message: ",bcolors.ENDC, decrypted_message)


# text function for rsa for encrypting and decrypting text
def check_rsa_text():

    print(bcolors.OKGREEN+"\nRSA for text\n",bcolors.ENDC)
    length = 5

    # generating 5 digit prime numbers
    p1= rsa.generatePrimeNumber(length)
    p2= rsa.generatePrimeNumber(length)

    # message to be encrypted
    msg = 'RSA by Joshua and Ishan'

    # printing parameter used
    print(bcolors.OKBLUE+"Parameters used\n",bcolors.ENDC)
    print("p1 is {} and p2 is {}".format(p1,p2))
    n,c,d = rsa.keygen(p1,p2)
    print('n, c, d is ', n,c,d)
    enc = rsa.encrypt(msg, n, c)
    print(bcolors.OKBLUE+'Encrypted Message',bcolors.ENDC + '{}'.format(enc))
    dec = rsa.decrypt(enc, n, d)
    print(bcolors.OKBLUE+'Decrypted Message',bcolors.ENDC + '{}'.format(dec))


# test function for el gamal with user prompt
def el_gamal_user_prompt():

    # intializing all as none
    keys = None
    cipher = None

    # asking user for input
    while True:
        value = input(
         bcolors.OKBLUE+"\nChoose 1 for generating key, 2 for encrypting message, 3 for decrypting message, 4 for quitting the program.:\n"+bcolors.ENDC)
        # input generate key
        if value == "1":
            keys = elgamal.generate_keys()
            priv = keys['privateKey']
            pub = keys['publicKey']
            print(bcolors.OKGREEN+"Key generated.\n",bcolors.ENDC)
            cipher = None
        # input encrypt message
        elif value == "2":
            if keys is None:
                print(bcolors.WARNING+"Generate key first.\n",bcolors.ENDC)
                continue
            else:
                message = input(bcolors.OKBLUE+"Enter message:"+bcolors.ENDC)
                cipher = elgamal.digit(pub, str(message))
                print(bcolors.OKGREEN+"Message encrypted\n",bcolors.ENDC)
        # input decrypt message
        elif value == "3":
            if cipher is None:
                print(bcolors.WARNING+"No message encrypted. Encrypt first\n",bcolors.ENDC)
            else:
                decrypted_message = elgamal.decipher(priv, pub, cipher)
                print(bcolors.OKGREEN+"The encrypted message is:",bcolors.ENDC, cipher, "\n")
                print(bcolors.OKGREEN+"The message received is:",bcolors.ENDC, decrypted_message, "\n")
        else:
            break

    
# calling the functions
check_rsa_text()

# uncomment for image and audio encryption

# rsa_image.start()
# rsa_audio_enc_dec.encrypt()
# rsa_audio_enc_dec.decrypt()
check_goldwasser()
check_el_gamal()
el_gamal_user_prompt()