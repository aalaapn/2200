import matplotlib.pyplot as pyplot
import numpy

x =  numpy.array([1,2,3,4,5])
y = numpy.array([2,2,2,5,5])

pyplot.figure()
pyplot.plot(x,y, linestyle = '--', marker = 'o', color = 'y' )
pyplot.title('B.3.')
pyplot.xlabel('X axis')
pyplot.ylabel('Y axis')
pyplot.show()


