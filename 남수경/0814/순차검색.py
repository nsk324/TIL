def sequenstialSearch2(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i = i+1
    if i<n and a[i] != key:
        return i
    else:
        return -1

data =  [1,2,3,4,5,6,7,8,9,10,100,101]
key = 11

print(sequenstialSearch2(data, len(data), key))