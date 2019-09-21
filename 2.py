a=input('kata 1: ')
b=input('kata 2: ')
c=input('kata 3: ')
d=input('kata 4: ')
word=[a,b,c,d]

def text(uji):
    for i in range(len(word)):
        simpan=''
        x=word[i] in uji
        print(simpan+word[i]+"="+str(x))

#contoh:
#a=bulan
#b=itu
#c=cantik
#d=sekali
#print(text('bungamatahariitucantuk'))
