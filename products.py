products = []
while True:
	name = input('请输入商品名称：')
	if name =='q':
		break
	price = input('请输入商品价格：')
	#p = []
	#p.append(name)
	#p.append(price)
	#products.append(p)
	products.append([name,price])
print(products)
print(products[0][0])

