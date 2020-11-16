# importing all the libraries
import sys
import time
import numpy
import scipy.io.wavfile
import matplotlib.pyplot as plt
from tqdm import tqdm


# function to decrypt audio file
def decrypt():

	start = time.time()
	fs, data = scipy.io.wavfile.read('./asymmetric_encryption/rsa_audio/encrypted.wav')

	# print audio file data to the screen
	print(data)
	print(fs)
	print(type(data))
	dataarray = data
	print(type(dataarray))
	a1, b1 = dataarray.shape
	tup1 = (a1, b1)
	data = data.astype(numpy.int16)
	data.setflags(write=1)
	print((a1,b1))

	# saving data to text file
	numpy.savetxt('./asymmetric_encryption/rsa_audio/txtaudio.txt', data)
	data= data.tolist()

	# showing the preogress bar
	for i1 in tqdm(range(len(data))):
		for j1 in (range(len(data[i1]))):
			x1 = data[i1][j1] 
			x1 = (pow(x1, 16971)%25777)
			data[i1][j1] = x1

	data = numpy.array(data)
	data = data.astype(numpy.uint8)
	print(data)

	# writing the output file to the filesystem
	scipy.io.wavfile.write('./asymmetric_encryption/rsa_audio/decrypted.wav', fs, data)

	# keeping track of the time taken for decryption
	end = time.time()
	ElspTime = (end-start)
	print('\n Total time taken : ', +ElspTime, 'sec')


# function to encrypt audio file
def encrypt():
	start = time.time()

	# reading the original audio file
	fs, data = scipy.io.wavfile.read('./asymmetric_encryption/rsa_audio/original.wav')
	
	# printing in a comprehensible manner
	print(data)
	print(fs)
	print(type(data))
	dataarray = data
	print(type(dataarray))
	a, b = dataarray.shape
	tup = (a, b)
	data = data.astype(numpy.int16)
	data.setflags(write=1)
	print((a,b))

	Time= numpy.linspace(0, len(data)/fs, num=len(data))

	# plotting the file as waves
	fig=plt.figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
	fig.add_subplot(1,2, 1)
	plt.xlabel('Audio wave')
	plt.plot(Time, data) 

	# encrypting 
	for i in range(0, tup[0]):
		for j in range(0, tup[1]):
			x = data[i][j] 
			x = ((pow(x,3)) % 25777)
			data[i][j] = x

	print(data)
	data = data.astype(numpy.int16)

	# writing to output file
	scipy.io.wavfile.write('./asymmetric_encryption/rsa_audio/encrypted.wav', fs, data)

	# displaying the encrypted audio as waves
	Time= numpy.linspace(0, len(data)/fs, num=len(data))
	fig.add_subplot(1,2, 2)
	plt.plot(Time, data) 
	plt.xlabel('Encrypted audio wave')
	plt.show(block='True')


	# keeping track of the encryption time
	end = time.time()
	ElspTime = (end-start)
	print('\n Total time taken: ', +ElspTime, 'sec')


