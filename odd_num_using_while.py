
		
		
		
		
# odd numbers program using while loop
x = int(input("enter the min number: "))
y = int(input("enter the max number: "))
i = x
if i%2==0:
	i = i+1
	while i<=y:
		print(i)
		i+=2
