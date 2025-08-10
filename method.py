class phone:
    price=1200
    color='black'
    brand='apple'
    feature=['camera','speaker','hammer']
    
    def call(self):
        print('calling someone')

    def send_sms(self,phone,sms):
        text=f'sending SMS to:{phone} and meassage:{sms}'
        return text
    
my_phone=phone()
print(my_phone.feature)
my_phone.call()
res=my_phone.send_sms(41529,'i am busy')
print(res)
