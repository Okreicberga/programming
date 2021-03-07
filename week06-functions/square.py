num = float(input("Enter a positive number: "))
a = 1.0

while(1):
	b = a*a
	if  num-0.1 < b < num+0.1 :
		break
	else:
		pass
	a = a + 0.01


print("\n Square root is: ",round(a,2))