import parser
import sys

def error():
	print "usage: python ern0i.py [-d] /face set/"
	sys.exit()

args = sys.argv[1:]

if not (0 < len(args) < 3):
	error()

if args[0] == '-d':
	flags = [1]
	set = args[1]
else:
	flags = [0]
	set = args[0]

if '/' not in set:
	error()
	
x = raw_input(set)
while x:
	try:
		parser.interpret(set + x, flags)
	except IndexError:
		print "IndexError"
	except SyntaxError:
		print "SyntaxError"	
	x = raw_input(set)

## 
# Taking input with ? or : from the interactive interpreter will 
# probably not work. 
##