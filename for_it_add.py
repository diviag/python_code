#!/usr/bin/env python2

#user input number add
import sys
import time
user_input=sys.argv[1:]
sum=0
print "processing......"
for i in user_input:
	sum = sum+ int(i)
	time.sleep(1)
print sum

