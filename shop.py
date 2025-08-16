class shop:
    cart=[]     #is a class attribute
    def __init__(self,buyer):
        self.buyer=buyer
    def add_to_cart(self,item):
        self.cart.append(item)



alina=shop('alina')
alina.add_to_cart('shoe')
alina.add_to_cart('phone')
print(alina.cart)

nish=shop('nish')
nish.add_to_cart('bike')
nish.add_to_cart('watch')
print(nish.cart)