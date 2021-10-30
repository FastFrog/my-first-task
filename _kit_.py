x = float(input("meaning x ="))
y = float(input("meaning y ="))
s = input("operator(+,-,/,*)=")
if s == "+":
    print(x+y)
elif s == "-":
    print(x-y)

elif s == "*":
    print(x*y)
elif s == "/":
    if y != 0:
        print(x/y)
    else:
        print("Error")

