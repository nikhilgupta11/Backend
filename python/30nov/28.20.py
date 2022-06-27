str1='James'
print("Original String is", str1)

res=str1[0]

l=len(str1)

mi=int(l/2)
res=res+str1[mi]

res=res+str1[l-1]
print("New String:", res)