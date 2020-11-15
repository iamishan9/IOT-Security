import sys
import time
import numpy
import scipy.io.wavfile
import matplotlib.pyplot as plt
from tqdm import tqdm

def decrypt():
	start = time.time()

	#Decryption

	fs, data = scipy.io.wavfile.read('./asymmetric_encryption/rsa_audio/encrypted.wav')
	print(data)
	print(fs)
	print(type(data))
	dataarray = data
	print(type(dataarray))
	a1, b1 = dataarray.shape
	tup1 = (a1, b1)
	data = data.astype(numpy.int16)
	#print(data.flags)
	data.setflags(write=1)
	#print(data.flags)
	print((a1,b1))
	numpy.savetxt('./asymmetric_encryption/rsa_audio/txtaudio.txt', data)
	data= data.tolist()

	for i1 in tqdm(range(len(data))):
		for j1 in (range(len(data[i1]))):
			x1 = data[i1][j1] 
			x1 = (pow(x1, 16971)%25777)
			data[i1][j1] = x1

	data = numpy.array(data)
	data = data.astype(numpy.uint8)
	print(data)
	scipy.io.wavfile.write('./asymmetric_encryption/rsa_audio/decrypted.wav', fs, data)

	end = time.time()
	ElspTime = (end-start)
	print('\n Total time taken : ', +ElspTime, 'sec')


def encrypt():
	start = time.time()

	#Encryption
	fs, data = scipy.io.wavfile.read('./asymmetric_encryption/rsa_audio/original.wav')
	print(data)
	print(fs)
	print(type(data))
	dataarray = data
	print(type(dataarray))
	a, b = dataarray.shape
	tup = (a, b)
	data = data.astype(numpy.int16)
	data.setflags(write=1)
	#print(data.flags)
	print((a,b))

	Time= numpy.linspace(0, len(data)/fs, num=len(data))

	fig=plt.figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
	fig.add_subplot(1,2, 1)
	plt.xlabel('Audio wave')
	plt.plot(Time, data) 

	# plt.show()
	for i in range(0, tup[0]):
		for j in range(0, tup[1]):
			x = data[i][j] 
			x = ((pow(x,3)) % 25777)
			data[i][j] = x

	print(data)
	data = data.astype(numpy.int16)
	scipy.io.wavfile.write('./asymmetric_encryption/rsa_audio/encrypted.wav', fs, data)

	Time= numpy.linspace(0, len(data)/fs, num=len(data))
	fig.add_subplot(1,2, 2)
 
	# plt.title('Encrypted Signal Wave')
	plt.plot(Time, data) 
	plt.xlabel('Encrypted audio wave')
	plt.show(block='True')
	# plt.show()

	end = time.time()
	ElspTime = (end-start)
	print('\n Total time taken: ', +ElspTime, 'sec')


