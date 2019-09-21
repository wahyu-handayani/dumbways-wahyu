import random
def acak(n):
    x="abcdefghijklmnopqrstuvwxyz0123456789"
    for i in range(n):
        tampil = ''.join(random.sample(x,4))
        tampil2 = ''.join(random.sample(x,4))
        tampil3= ''.join(random.sample(x,4))
        tampil4 = ''.join(random.sample(x,4))
        print(tampil+"-"+tampil2+"-"+tampil3+"-"+tampil4)
#contoh:
#jalankan acak(250)