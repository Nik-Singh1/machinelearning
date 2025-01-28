x = [16,9,5,17]
for i in range(len(x)):
	for j in range(0,len(x)-i-1):
		if x[j]>x[j+1]:
			x[j], x[j+1]=x[j+1],x[j]
print("reversed list is:", x)