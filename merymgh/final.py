import sys
import numpy
from matplotlib import pyplot as plt

def main():
	script = sys.argv [0]
	fname = sys.argv [1]
	data = numpy.loadtxt (fname, delimiter = ",", skiprows = 1, usecols = range (1,13))
	for m in data.mean(axis =0):
		print (m)
		
	y= data.mean (axis = 0)
	x = numpy.arange (len(y))
	fig = plt.figure()
	axes = fig.add_subplot(1,1,1)
	axes.bar(x,y,0.5)
	axes.set_ylabel ("average")
	axes.set_xlabel ("years")
	data2 = numpy.loadtxt (fname, delimiter = ",", dtype = "str", usecols = range (1,13))
	ax = data2[0,0:13]
	axes.set_xticks (x)
	axes.set_xticklabels(ax)
	axes.set_title ("final.png")
	fig.tight_layout()
	plt.show()
main()