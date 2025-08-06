class Bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw=40000

    def get_balance(self):
        return self.balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
    
    def withdraw(self,amount):
        if amount<self.min_withdraw:
            print (f'You are too gorib to withdraw')
        elif amount>self.max_withdraw:
            print(f'Choose another balance less than{self.max_withdraw}') 
        else:
            self.balance-=amount
            print(f'Successfully withdrawn {amount}') 
    


brac=Bank(100000000000)
brac.withdraw(30)
brac.withdraw(100000000000000)
brac.withdraw(1000)



    