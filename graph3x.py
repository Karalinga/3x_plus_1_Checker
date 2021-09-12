#3x+1 problem with graph
import turtle
count = 0
t = turtle.Pen()
x = int(input("Enter your number: "))
while(x!=1):
	if(x%2==0):
		x = int(x/2)
	else:
		x = 3*x +1
	count +=10
	t.goto(count,x)
	print(x)