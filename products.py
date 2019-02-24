#读取档案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品, 价格' in line:
			continue #继续
		name, price = line.strip(). split(',')
		products.append([name, price])

print(products)

#存数据

while True:
	name = input('请输入商品名称：')
	if name =='q':
		break
	price = input('请输入商品价格：')
	#p = []
	#p.append(name)
	#p.append(price)也可以看下面

	#p = [name. price]也可以看下面

	products.append([name, price])
#print(products)


for p in products:
	#print (p)
	#print(p[0])就是映出商品名称
	print(p[0], '的价格是', p[1])
#  products[0][0] #取出数据

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品, 价格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')