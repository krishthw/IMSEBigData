#!/usr/bin/env python

import csv
import sys

SEP = "\t"

class Mapper(object):

	def __init__(self, stream, sep=SEP):
		self.stream = stream				# read M.csv as a stream
		self.sep    = sep					# seperator to identyfy input/output '\t' by default
		self.V = {}                         # make a dictionary to store vector V values
		with open ("vector.csv", "r") as f: 
			for line in f:
				line = line.replace('\t',',')
				source, pagerank = line.split (',')
				self.V[int(source)] = float(pagerank) 

	def emit(self, key, source, weight, pagerank):
		sys.stdout.write("%s%s%s%s%s%s%s\n" % (key, self.sep,source,self.sep ,weight,self.sep,pagerank))

	def map(self):
		reader = csv.reader(self.stream) 
		# sort by destination
		for source, dest, weight in sorted(reader,key=lambda row : int(row[1])): 
			dict_key=int(source)
			# emit key =destination and value=(source,M and pagerank)
			self.emit(key=dest, source=source, weight=weight, pagerank=self.V[dict_key]) 

if __name__ == '__main__':
 	mapper = Mapper(sys.stdin)
 	mapper.map()
