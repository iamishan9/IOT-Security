from asymmetric_encryption import goldwasser

def check_goldwasser():
    m = '10000100000100101100'
    # m='1001'
    
    p = 499
    q = 547
    # p=19
    # q=7
    # n=p*q
    a = -57
    b = 52
    # a=3
    # b=-8
    x0 = 159201
    
    
    c, xt = goldwasser.BGW_enc(p, q, a, b, x0, m)
    print ("ciphertext:", c, "and x is",xt)
    d = goldwasser.BGW_dec(p, q, a, b, xt, c)
    
    print ("asserting that decrypted plaintext == m...")
    print('decrypted is {}'.format(d))
    
    if m==d:
        print ("assertion correct! done.")


check_goldwasser()