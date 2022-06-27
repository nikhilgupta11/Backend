a=list(input("enter your first list = "))
b=list(input("enter your second list = "))

# a = ["nikhil", "full stake"] 
# b = ["gupta", "developer"]
c = [i + j for i, j in zip(a, b)]
print(c)