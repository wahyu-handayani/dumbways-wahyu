num = int(input("Masukkan tanggal: "))
uang = int(input("Masukkan uang: "))
telur=2500
butir=uang//2500
lusin=butir//12
if num >= 1 and num <= 31:
    for i in range(2,num):
        #bukan prima
        if (num % i) == 0:
            if num%2==1:
                bonus=3*lusin
                if num%5==0 and bonus%2==0:
                    bonus=bonus*10
                elif num%5==0 and bonus%2==1:
                    bonus=bonus*5
                total=butir+bonus
            break
        else:
            #prima
            if lusin>=1:
                bonus=2*lusin
                if num%5==0 and bonus%2==0:
                    bonus=bonus*10
                elif num%5==0 and bonus%2==1:
                    bonus=bonus*5
                total=butir+bonus
print("Total Telur: ",total)
            
