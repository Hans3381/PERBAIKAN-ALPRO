import math
def menghitung(n):
    total = 0
    i = 1
    while i <= n :
        total += i
        i += 1
    return total
n = int(input("masukkan n : "))
hasil = menghitung(n)
print(f"total :{hasil}")