# import numpy
# def clip(x):
# 	y = x
# 	for i in numpy.nditer(y, op_flags=['readwrite']):
# 		if i[...] < 5:
# 			i[...] = 5
# 	return y

# x = numpy.array([3,8,6,2,7])
# clip = clip(x)
# print clip

import numpy
import matplotlib.pyplot as pyplot
x = numpy.array([1,2,3,4,5])
y = numpy.array([9,8,7,6,5])

pyplot.figure
pyplot.plot(x,y,linestyle='--', marker='o', color='r')
pyplot.title('Title Bitches')
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.tight_layout()
pyplot.show()

