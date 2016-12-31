import parser
import sys
import re

arguments = sys.argv[1:]

if not arguments:
	print "usage: python ern0.py [-d] file ..."
	sys.exit()

##
# The only flag currently available is the debug flag which displays 
# the pointer location and the corresponding cube and the end of the 
# program's run. I expect to add more in the future
##
options = [0]
if arguments[0][0] == '-':
	flags = arguments.pop(0)
	if 'd' in flags:
		options[0] = 1
		
for file in arguments:
	if not re.match('.*\.rn$', file):
		continue
	print file
	with open(file, 'r') as f:
		parser.interpret(f.read(), options)
	