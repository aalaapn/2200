import numpy as np
import matplotlib.pyplot as plt
def concat(x):
	y=x[:]

	return y

x=np.array([[1,2,3],[1,2,3]])
print x[1]

y = concat(x)
print y


#impulse
x = np.zeros(100)
x[4] = 1
y=np.arange(0,100,1)
plt.figure()
plt.stem(y,x)
plt.show()


#generate signal
t=np.arange(0,10,.1)
x = np.cos(2*np.pi*t)
y = np.exp(t*(-.9))*np.cos(2*np.pi*t)
f, (ax1, ax2) = plt.subplots(1,2,sharey=False)
ax1.plot(t, y)
ax2.plot(t,x)
ax1.set_title('C.1.')
ax2.set_title('C.2.')
plt.show()


#Subplot
t=np.arange(0,10,.1)
x = np.cos(2*np.pi*t)
y = np.exp(t*(-.9))*np.cos(2*np.pi*t)
f, (ax1, ax2) = plt.subplots(1,2,sharey=False)
ax1.plot(t, y)
ax2.stem(t,x)
ax1.set_title('C.1.')
ax2.set_title('C.2.')
plt.show()

#my_echo
def my_echo(x,d,a):
	freq = 100
	plt.figure()

	delay = np.zeros(d*freq)
	fin = np.concatenate((x, delay),axis= 0)
	echo_duration=np.arange(1,(x.size*a))
	fin2 = np.concatenate((fin, echo_duration),axis = 0)
	y=np.arange(0,((fin2.size/freq))+.99,.01)
	print y.size
	print 'asdfasdlkfjas;ldkfj'
	print fin2.size
	print "llpalplasdpflaspdflpasldfpalsdfplasdpflaspdfl"
	print fin2
	plt.plot(y,fin2)
	plt.title('Echo')
	plt.ylabel('Signal Amplitude')
	plt.xlabel('Time in sec')
	plt.show()
	

my_echo(np.arange(0,15000),50,.5)
