import math, ast 
from collections import defaultdict
import dimensions 


# Open the log file 
def openLog(path,d): 
	lines = open(path, 'r').readlines()
	for line in lines: 
		print line
		coords, actual, guess, score = line.split('\t')
		print coords, actual, guess, score 
		# d[coords].extend([(actual,guess)])
	# return d 

new = dict()
print openLog('log.txt', new)




	