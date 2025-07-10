def full_name(first,last):
    name =f'{first} {last}'
    return name 

name =full_name('asad','fagun')
print(name)
# ** means kargs
def famous_name(first,last,**addition):
    name=f'{first} {last}'
    for key,values in addition.items():
        print(key,values)
    return name

name=famous_name(first='tahir',last='ali',title3='hujur',title='shayek',title2='shah',last2='taheri')
print(name)
#return multiple form function
def a_lot(num1,num2):
    sum=num1+num2
    mul=num1*num2
    remain=num1-num2
    return sum,mul,remain

ev=a_lot(22,11)
print(ev)