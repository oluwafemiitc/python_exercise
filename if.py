price = input ('What price is the item: ')

price = float(price)
if  price <= 1:
    tax = 0.7
    print (' The tax is : '+ str(tax))


else:
    tax= 0.2
    print('The tax of : '+ str(price) +' 1is = ' + str(tax))

