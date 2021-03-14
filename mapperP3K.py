#!/usr/bin/env python

import csv
import sys

SEP = "\t"

class Mapper(object):

	def __init__(self, stream, sep=SEP):
		self.stream = stream
		self.sep    = sep

	def emit(self, key, value):
		sys.stdout.write("%s%s%s\n" % (key, self.sep, value))

	def map(self):
		reader = csv.reader(self.stream)
		for row in reader:
                        for i in sorted(reader,key=lambda row : int(row[1])): #sort values according to csv row[1]
                                self.emit(i[1], i[2])

if __name__ == '__main__':
 	mapper = Mapper(sys.stdin)
 	mapper.map()
