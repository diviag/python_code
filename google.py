#!/usr/bin/env python2

import urllib2
from googlesearch import search

# now put a keyword
webdata= search('hello',num=1)

# generator type iterable

for i in webdata:
	print i 
	link = urllib2.urlopen(i)
	print link.read
