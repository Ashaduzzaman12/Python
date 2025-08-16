class Shopping :
    def __init__(self,name):
        self.name=name
        self.cart=[]


    def add_to_cart(self,item,price,quantity):
        product={'item': item,'price':price,'quantity':quantity}
        self.cart.append(product)

    def remove_item(self,item):
        
    def checkout(self,amount):
        total=0
        for item in self.cart:
            total+= item['price']* item['quantity']
        print('total Price',total)
        if(amount<total):
            print(f'please provide {total -amount} taka more')
        else:
            extra=amount-total
            print(f'Here is youe extra money {extra}') 
jolil=Shopping('ananta jolil')

jolil.add_to_cart('alu',40,6)
jolil.add_to_cart('dim',12,24)
jolil.add_to_cart('rice',90,10)

print(jolil.cart)
jolil.checkout(1600)