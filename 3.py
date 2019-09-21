d = [50000, 20000, 10000, 5000, 2000, 1000, 500]
def hasil(total_belanja,jum_uang):
    kembalian=jum_uang-total_belanja
    for x in range(len(d)):
        simpan=''
        i=0
        while kembalian >= d[x]:
            kembalian = kembalian-d[x]
            i = i+1
        if (i>0):
            print(simpan+str(i)+" lembar "+str(d[x]))


