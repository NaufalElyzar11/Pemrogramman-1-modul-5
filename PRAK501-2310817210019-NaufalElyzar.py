def max_bilangan(a, b, c, d):
    maks = a  

    if b > maks:
        maks = b 

    if c > maks:
        maks = c 

    if d > maks:
        maks = d  

    return maks  


a, b, c, d = map(int, input().split())
hasil = max_bilangan(a, b, c, d)
print(hasil)
