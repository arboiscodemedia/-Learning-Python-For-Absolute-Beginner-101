nterms = input("How many terms?")
nterms = int(nterms)

n1, n2 = 0, 1

if nterms <= 0:
    print("Please enter a positive number")
elif nterms == 1:
    print("Fibonacci sequence up to",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    count = 0
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
        
