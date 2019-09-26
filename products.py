products=[]
while True:
	name=input('What do you whant to buy?(end to end)')
	if name=='end':
		break
	price=input('What is the price?')
	products.append([name,price])
#print(products)
for p in products:
	print(p[0],'is',p[1])
with open('products.csv','w') as f:
	for p in products:
		f.write(p[0]+','+p[1]+'\n')