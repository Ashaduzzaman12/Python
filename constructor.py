class phone :
    manufec='china'

    def __init__(self,brand,price,owner):
        self.owner=owner
        self.brand=brand
        self.price=price


    def sms_send(self,phone,sms):
        txt=f'send to :{phone} {sms}'
        print(txt)


my_phn=phone('xiaomi','990','kopa samsu')
print(my_phn.owner,my_phn.price,my_phn.brand)

her_phn=phone('iphone','990','babygirl')
print(her_phn.owner,her_phn.price,her_phn.brand)