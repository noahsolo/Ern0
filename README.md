# Ern0
An programming language based around the Rubik's Cube
In Ern0, one works with an 'infinite' tape of 2x2x2 Rubiks Cubes.
Each cube represents 6 2x2 matrices which shift as the programmer turns the layers of the cubes.

## SYNTAX RULES ##
/././././././ set FLUDRB faces in order (must start program)
/n/		synonym of /n/n/n/n/n/n/
/$/		synonym of /0/1/2/3/4/5/

F		front face clockwise
L		left face clockwise
U		up face clockwise
D		down face clockwise
R		right face clockwise
B		back face clockwise
'		counterclockwise move
2		do previous move again

[		while current cube is unsolved
]		end while loop

>		next cube, create cube
<		previous cube
$1	    jump to cube

(a+b)	matrix sum to current cube
(a*b)	matrix product to current cube
		a and b are code snippets; how you would access cube A and cube B from
		current position (with '>', '<' or jumps)

;		output determinant of front face as ascii
:		input ascii x to front face as [[x 0] [0 1]]
!		output determinant of front face as decimal
?		input decimal x to front face as [[x 0] [0 1]]

#		open/close comment
