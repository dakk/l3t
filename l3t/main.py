#!/usr/bin/python3

# MIT License

# Copyright (c) 2021 Davide Gessa

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys 
import getpass
import argparse

if sys.version_info[0] < 3:
	print ('python2 not supported, please use python3')
	sys.exit (0)

try:
	import requests
except:
	print ('please install requests library (pip3 install requests)')
	sys.exit (0)


from .lmodules import *
from .lisk_node import LiskNode


# Parse command line args
def parseArgs():
	usage = '''usage: l3t [-h] action [arguments]

Lisk3 node management tool

actions:
'''
	for x in LMODULES:
		usage += '  %s\t\t%s\n' % (x.NAME, x.DESCRIPTION)

	parser = argparse.ArgumentParser(usage=usage)

	# parser.add_argument('action', metavar='action', type=str, help="action to run")	
					
	# parser.add_argument('--network', type=str, dest='network', action='store',
	#  			   default=None,
	#  			   help='force network to mainnet or testnet (default: auto)')

	base = getpass.getuser()
	if base == 'root':
		base = '/root/'
	else:
		base = '/home/%s/' % base

	parser.add_argument('--base-path', type=str, dest='basepath', action='store',
	 			   default=base,
	 			   help='set base path (default: %s)' % base)

	return parser

def getActionModule(act):
	if act:
		for x in LMODULES:
			if x.NAME == act:
				return x

def main():
	parser = parseArgs() 

	if len(sys.argv) < 2:
		parser.print_help()
		sys.exit(0)

	module = getActionModule(sys.argv[1])

	if module == None:
		print ('Unknown action: %s' % sys.argv[1])
		sys.exit(0)

	lnode = LiskNode()
	m = module(parser, lnode)
	m.parseArgs()
	m.run()

	print ('Done.')

if __name__ == "__main__":
	main()