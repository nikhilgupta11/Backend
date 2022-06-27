salary=int(input("enter your salary"))

tax=0
if salary<=10000:
    tax=0

elif salary<=20000:
    a=salary-10000
    tax=a*10/100

else:
    tax=0
    tax=10000*10/100
    tax+=(salary-20000)*20/100

print(tax)
