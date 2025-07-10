balance=3000
#if we want to edit global variable in function than we need global keyword
def buy_thing(item,price):
    global balance
    balance=balance-price
    print(f'balance after buying {item}',balance)
buy_thing('sunglass',1000)