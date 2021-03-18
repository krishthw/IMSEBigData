#!/usr/bin/env python

import sys

from itertools import groupby
from operator import itemgetter

SEP = "\t"

class Reducer(object):

	def __init__(self, stream, sep=SEP):
		self.stream = stream
		self.sep    = sep

	def emit(self, key, pagerank):
		sys.stdout.write("%s%s%s\n" % (key, self.sep, pagerank))
	

	def reduce(self):
		for current, group in groupby(self, itemgetter(0)):
			total = 0 

			for item in group:
				total += float(item[2])*float(item[3])

			self.emit(current, float(total))

	def __iter__(self):
		for line in self.stream:
			try:
				parts = line.split(self.sep)
				yield parts[0], int(parts[1]),float(parts[2]),float(parts[3])
			except:
				continue

if __name__ == '__main__':
	reducer = Reducer(sys.stdin)
	reducer.reduce()
