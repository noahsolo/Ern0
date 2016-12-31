import re
import operator as op

class Cube(object):

	def __init__(self, faces=[0, 1, 2, 3, 4, 5]):
		# (0, 1, 2, 3, 4, 5) = (F, L, U, D, R, B)
		self.c = [[i] * 4 for i in faces]
		

	def cycle(self, d, k):
		if not k:
			d.reverse()
		shelf = self.c[d[0][0]][d[0][1]]
		for i in range(0, len(d) - 1):
			x1, y1 = d[i]
			x2, y2 = d[i + 1]
			self.c[x1][y1] = self.c[x2][y2]
		self.c[x2][y2] = shelf
			
	def F(self, k=True):
		self.cycle([(0, 0), (0, 2), (0, 3), (0, 1)], k)
		self.cycle([(2, 2), (1, 3), (3, 1), (4, 0)], k)
		self.cycle([(2, 3), (1, 1), (3, 0), (4, 2)], k)
			
	def L(self, k=True):
		self.cycle([(1, 0), (1, 2), (1, 3), (1, 1)], k)
		self.cycle([(2, 0), (5, 3), (3, 0), (0, 0)], k)
		self.cycle([(2, 2), (5, 1), (3, 2), (0, 2)], k)
	
	def U(self, k=True):
		self.cycle([(2, 0), (2, 2), (2, 3), (2, 1)], k)
		self.cycle([(0, 0), (4, 0), (5, 0), (1, 0)], k)
		self.cycle([(0, 1), (4, 1), (5, 1), (1, 1)], k)
	
	def D(self, k=True):
		self.cycle([(3, 0), (3, 2), (3, 3), (3, 1)], k)
		self.cycle([(0, 2), (1, 2), (5, 2), (4, 2)], k)
		self.cycle([(0, 3), (1, 3), (5, 3), (4, 3)], k)
	
	def R(self, k=True):
		self.cycle([(4, 0), (4, 2), (4, 3), (4, 1)], k)
		self.cycle([(2, 3), (0, 3), (3, 3), (5, 0)], k)
		self.cycle([(2, 1), (0, 1), (3, 1), (5, 2)], k)
	
	def B(self, k=True):
		self.cycle([(5, 0), (5, 2), (5, 3), (5, 1)], k)
		self.cycle([(2, 1), (4, 3), (3, 2), (1, 0)], k)
		self.cycle([(2, 0), (4, 1), (3, 3), (1, 2)], k)
		
	def alg(self, seq, n=1):
		f = lambda x: re.match('[FLUDRB]', x) and len(x) < 3
		seq = filter(f, re.split("([FLUDRB]['2]?)", seq))
		for m in range(0, n):
			for i in seq:
				eval("self.%s(%r)" % (i[0], "'" not in i))
				if "2" in i:
					eval("self.%s()" % i[0])
	
	def display(self):
		print "           ---------\n          | %3.f %3.f |\n          |     \
    |\n      %3.f | %3.f %3.f | %3.f\n --------- --------- ---------\n| %3.f \
%3.f | %3.f %3.f | %3.f %3.f |\n|                             |\n| %3.f %3.f \
| %3.f %3.f | %3.f %3.f |\n --------- --------- ---------\n      %3.f | %3.f \
%3.f | %3.f\n          |         |\n          | %3.f %3.f |\n           -----\
----" % (self.c[2][0], self.c[2][1], self.c[5][1], self.c[2][2], self.c[2][3], 
		self.c[5][0], self.c[1][0], self.c[1][1], self.c[0][0], self.c[0][1], 
		self.c[4][0], self.c[4][1], self.c[1][2], self.c[1][3], self.c[0][2], 
		self.c[0][3], self.c[4][2], self.c[4][3], self.c[5][3], self.c[3][0],
		self.c[3][1], self.c[5][2], self.c[3][2], self.c[3][3])
	
	def det(self):
		return (self.c[0][0] * self.c[0][3]) - (self.c[0][1] * self.c[0][2])
	
	def solved(self):
		for i in range(0, 6):
			if len(set(self.c[i])) != 1: 
				return False
		return True
	
def addc(a, b):
	output = Cube()
	for i in range(0, 6):
		output.c[i] = map(op.add, a.c[i], b.c[i])
	return output

def subc(a, b): # possibly implemented in the future
	output = Cube()
	for i in range(0, 6):
		output.c[i] = map(op.sub, a.c[i], b.c[i])
	return output

def dot(m, n):
	return sum(map(op.mul, m, n))

def chop(m):
	return [m[:2],m[2:]]

def mulc(a, b):
	output = Cube()
	for i in range(0, 6):
		a.c[i][1], a.c[i][2] = a.c[i][2], a.c[i][1]
		output.c[i] = [dot(m, n) for m in chop(a.c[i]) for n in chop(b.c[i])]
	return output
