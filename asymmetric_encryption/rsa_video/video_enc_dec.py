import os
import cv2
import time
import numpy
import imageio
from tqdm import tqdm
from skimage import io
from random import randrange, getrandbits

# Find D.
def gcdExtended(E, eulerTotient):
    a1, a2, b1, b2, d1, d2 = 1, 0, 0, 1, eulerTotient, E

    while d2 != 1:

        # k
        k = (d1//d2)

        # a
        temp = a2
        a2 = a1-(a2*k)
        a1 = temp

        # b
        temp = b2
        b2 = b1-(b2*k)
        b1 = temp

        # d
        temp = d2
        d2 = d1-(d2*k)
        d1 = temp

        D = b2

    if D > eulerTotient:
        D = D % eulerTotient
    elif D < 0:
        D = D+eulerTotient

    return D


# modular power
def power(a, d, n):
    ans = 1
    while d != 0:
        if d % 2 == 1:
            ans = ((ans % n)*(a % n)) % n
        a = ((a % n)*(a % n)) % n
        d >>= 1
    return ans

# miller rabin to check primality
def MillerRabin(N, d):
    a = randrange(2, N - 1)
    x = power(a, d, N)
    if x == 1 or x == N-1:
        return True
    else:
        while(d != N-1):
            x = ((x % N)*(x % N)) % N
            if x == 1:
                return False
            if x == N-1:
                return True
            d <<= 1
    return False


# check if number is prime
def is_prime(N, K):
    if N == 3 or N == 2:
        return True
    if N <= 1 or N % 2 == 0:
        return False
    # Find d such that d*(2^r)=X-1
    d = N-1
    while d % 2 != 0:
        d /= 2

    for _ in range(K):  
        # calling Miller rabin
        if not MillerRabin(N, d):
            return False
    return True

# generating prime candidate
def generate_prime_candidate(length):
    # generate random bits
    p = getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

# generating prime number
def generatePrimeNumber(length):
    A = 4
    while not is_prime(A, 128):
        A = generate_prime_candidate(length)
    return A




data = './data'
endata = './Endata'
dedata = './Dedata'

# generating P and Q
length = 5
P = generatePrimeNumber(length)
Q = generatePrimeNumber(length)

# printing them
print(P)
print(Q)


# Calculating N=P*Q and Euler Totient Function = (P-1)*(Q-1)
N = P*Q
eulerTotient = (P-1)*(Q-1)
print(N)
print(eulerTotient)

def GCD(a, b):
    if a == 0:
        return b
    return GCD(b % a, a)


E = generatePrimeNumber(4)
while GCD(E, eulerTotient) != 1:
    E = generatePrimeNumber(4)
print(E)

D = gcdExtended(E, eulerTotient)
print('D is ',D)
enc = [[[0 for x in range(320)] for y in range(240)] for z in range(68)]


# call encrypt function
def encrypt():
    load_image_encrypt(data)

# call decrypt function
def decrypt():
    load_image_decrypt(data)


# load folder for image encryptiong and carry out encryption
def load_image_encrypt(folder):

    videofile = 'video.avi'

    try:
        if not os.path.exists('Endata'):
            os.makedirs('Endata')
    except OSError:
        raise ValueError('No file')

    name = './data/frame'
    vid_to_image(name, videofile)



    for filename1 in tqdm(os.listdir(folder)):
        filenum = filename1.replace('frame','')
        filenum = filenum.replace('.png','')
        imgV = imageio.imread(os.path.join(folder, filename1))
        if imgV is not None:
            RGBencryption(imgV, filename1, filenum)
        else:
            break
    vidname = 'envid.avi'
    image_to_vid(endata, vidname)

    print('Finish!', 'Encryption Done succesfully!')

# load folder for image decryption and carry out decryption
def load_image_decrypt(folder):

    videofile = 'envid.avi'

    try:
        if not os.path.exists('Dedata'):
            os.makedirs('Dedata')
    except OSError:
        raise ValueError(
            'Error Occured', 'Error: Creating directory of decrypted data')

    name = './data/frame'
    vid_to_image(name, videofile)

    for filename1 in tqdm(os.listdir(folder)):
        # print('file is ', filename1)
        # file_num = filename[]
        filenum = filename1.replace('frame','')
        filenum = filenum.replace('.png','')
        imgV = imageio.imread(os.path.join(folder, filename1))
        if imgV is not None:
            RGBdecryption(imgV, filename1, filenum)
        else:
            break

    vidname = 'devid.avi'
    image_to_vid(dedata, vidname)

    print('Finish!', 'Decryption Done succesfully!')

# encryption using RSA
def RGBencryption(my_img, filename, num):
    num = int(num)
    height, width = my_img.shape[0], my_img.shape[1]
    # Encrypting image
    for i in range(0, height):
        for j in range(0, width):
            r, g, b = my_img[i, j]
            C1 = power(r, E, N)
            C2 = power(g, E, N)
            C3 = power(b, E, N)
            enc[num][i][j] = [C1, C2, C3]
            C1 = C1 % 256
            C2 = C2 % 256
            C3 = C3 % 256
            my_img[i, j] = [C1, C2, C3]
    name = './Endata/'+str(filename)
    imageio.imwrite(name, my_img, format='PNG-FI')


# decryption using RSA
def RGBdecryption(my_img, filename, num):
    num = int(num)
    height, width = my_img.shape[0], my_img.shape[1]
    # Decrypting image
    for i in range(0, height):
        for j in range(0, width):
            r, g, b = enc[num][i][j]
            M1 = power(r, D, N)
            M2 = power(g, D, N)
            M3 = power(b, D, N)
            my_img[i, j] = [M1, M2, M3]
    name = './Dedata/'+str(filename)
    imageio.imwrite(name, my_img, format='PNG-FI')

# convert video to images
def vid_to_image(foldername, filename):
    # Playing video from file:
    cap = cv2.VideoCapture(filename)

    try:
        if not os.path.exists('data'):
            os.makedirs('data')
        print(
            'Info!', 'Data directory is created where the frames are stored')

    except OSError:
        raise ValueError('Error: Creating directory of data')

    currentFrame = 0
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Saves image of the current frame in jpg file
        name = foldername + str(currentFrame) + '.png'
        print('Creating...' + name)
        imageio.imwrite(name, frame, format='PNG-FI')

        # To stop duplicate images
        currentFrame += 1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

# combine images to video
def image_to_vid(folder, vidname):

    image_folder = folder
    video_name = vidname
    sort_image = []
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    print(images)
    print('\n\n')

    for i in range(0, 1000):
        for j in range(len(images)):
            name = 'frame' + str(i) + '.png'
            if ((str(images[j])) == str(name)):
                sort_image.append(images[j])

    print(sort_image)
    frame = cv2.imread(os.path.join(image_folder, sort_image[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 29, (width, height))

    for image in sort_image:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

print('Encrypting')
encrypt()

print('\n\n\n\n')
print('Decrypting')
decrypt()
