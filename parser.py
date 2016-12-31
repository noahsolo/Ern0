import re
import sys
from matrubix import *

def tokenize(code):
	code = re.sub("#.+?#", '', code)
	patt = "(/(?:-?\d+/){6}|/[\$\d]/|(?:[FLUDRB]['2]?)+|[][><:;?!x]|\$\d+|\
\(.*?[\+\*].*?\))"
	return re.findall(patt, code)

pointer = None
readr = None
		
def interpret(source, flags = [0]):
	## Commands ##
	def succ(x):
		global pointer
		pointer += 1
		if not pointer < len(array):
			array.append(Cube(faces))

	def prev(x):
		global pointer
		pointer -= 1
		if pointer < 0:
			raise IndexError

	def moves(x):
		array[pointer].alg(x)
		
	def jump(x):
		global pointer
		pointer = int(x[1:])
		while not pointer < len(array):
			array.append(Cube(faces))

	def loopstart(x):	
		global readr
		if array[pointer].solved():
			depth = 1
			while s[readr] != ']' and depth:
				readr += 1
				if readr >= size:
					raise SyntaxError
				if s[readr] == '[':
					depth += 1
				elif s[readr] == ']':
					depth -= 1
		else:
			pass	
	
	def loopend(x):
		global readr
		depth = 1
		while s[readr] != '[' and depth:
			readr -= 1
			if readr < 0:
				raise SyntaxError 
			if s[readr] == ']':
				depth += 1
			elif s[readr] == '[':
				depth -= 1
		readr -= 1

	def goto(s): # not a command
		t = tokenize(s)
		p = pointer
		for i in t:
			if i == '>':
				p += 1
			elif i == '<':	
				p -= 1
			elif '$' in i:
				p = int(i[1:])
		if not 0 <= p < len(array):
			raise IndexError
		return p
	
	def adding(x):
		a, b = re.match('\((.*?)\+(.*?)\)', x).groups()
		array[pointer] = addc(array[goto(a)],array[goto(b)])
	
	def multiplying(x):
		a, b = re.match('\((.*?)\*(.*?)\)', x).groups()
		array[pointer] = mulc(array[goto(a)],array[goto(b)])

	def inpt(x):
		n = sys.stdin.read(1)
		if n:
			array[pointer].c[0] = [ord(n), 0, 0, 1]

	def outpt(x):
		n = array[pointer].det()
		if 0 <= n < 256:
			sys.stdout.write(chr(n))

	def inptd(x):
		#TODO
		raise NotImplementedError 

	def outptd(x):
		sys.stdout.write(str(array[pointer].det()))
	
	def reset(x):
		array[pointer] = Cube(faces)
	## End Commands ##
	
	global pointer
	global readr
	pointer = 0
	readr = 0
	s = tokenize(source)
	array = []

	head = s[0][1:-1]
	if head == '$':
		faces = [0, 1, 2, 3, 4, 5]
	else:
		try:
			faces = [int(head)] * 6
		except:
			m = re.match("(-?\d+)/(-?\d+)/(-?\d+)/(-?\d+)/(-?\d+)/(-?\d+)", 
				head)
			try:
				faces = [int(m.group(i)) for i in range(1, 7)]
			except:
				raise SyntaxError

	array.append(Cube(faces))
	s = filter(lambda x: '/' not in x, s)
	size = len(s)
	
	while readr < size:
		expr = s[readr]
		lex = ['>','<',"([FLUDRB]['2]?)+",'\$\d+','\[','\]','\(.*?\+.*?\)',
			'\(.*?\*.*?\)',':',';','\?','!', 'x']
		x = -1
		for i in range(0, len(lex)):
			if re.match(lex[i], expr):
				x = i; break
		{
			0: succ,
			1: prev,
			2: moves,
			3: jump,
			4: loopstart,
			5: loopend,
			6: adding,
			7: multiplying,
			8: inpt,
			9: outpt,
			10: inptd,
			11: outptd,
			12: reset
		}[x](expr)
		
		readr += 1
	
	sys.stdout.write("\n")
	if flags[0]:
		print pointer
		array[pointer].display()	 
	
