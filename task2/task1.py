def bin(x):
    b= ''
    while x>0:
        rev=x%2
        b= str(rev) + b
        x=x//2
    return b
def bincheck(binary):
    for i in range(0, (len(binary)-1)):
        c=0
        if binary[i]=='1'and binary[i+1]=='1':
            condition=True
            c+=1
            break
        else:
            continue
    if c==0:
        condition=False
    return condition

def check(x,y):
    final={}
    for num in range(x, y):
        binary = bin(num)
        condition = bincheck(binary)
        number = {num: condition}
        final.update(number)
    return final
x=int(input("Enter starting number: "))
y=int(input("Enter ending number: "))
check(x,y)
