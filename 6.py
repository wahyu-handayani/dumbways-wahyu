def SUM(n,x,y,z):
    digit=""
    for i in range(n):
        digit=digit+str(i+1)
    jum=int(digit[x-1])+int(digit[y-1])+int(digit[z-1])
    return jum
def MUL(n,x,y,z):
    digit=""
    for i in range(n):
        digit=digit+str(i+1)
    minus=int(digit[x-1])-int(digit[y-1])-int(digit[z-1])
    return minus
def SUB(n,x,y,z):
    digit=""
    for i in range(n):
        digit=digit+str(i+1)
    kali=int(digit[x-1])*int(digit[y-1])*int(digit[z-1])
    return kali
def DIV(n,x,y,z):
    digit=""
    for i in range(n):
        digit=digit+str(i+1)
    bagi=int(digit[x-1])/int(digit[y-1])/int(digit[z-1])
    return bagi

