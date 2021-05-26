def firstNatural_number(n):
    if n <= 1:
        return 1
    else:

        return n + firstNatural_number(n-1)

num = int(input("Enter number : "))
f = firstNatural_number(num)

if(num <= 1):
    print("Plz Enter Postive Number : ")
else:
    print(f)

