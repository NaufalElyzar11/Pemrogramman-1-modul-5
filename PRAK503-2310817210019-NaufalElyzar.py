def maksimal(a, b):
    return a if a > b else b

def minimal(a, b):
    return a if a < b else b

batas = int(input())
bilangan = list(map(int, input().split()))

maks = float('-inf')
minim = float('inf')

for nilai in bilangan:
    maks = maksimal(maks, nilai)
    minim = minimal(minim, nilai)

print(f"{maks} {minim}")
