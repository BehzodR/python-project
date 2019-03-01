n=input("Enter a number")
while type(n)!=int:
    try:
        n=int(n)
    except ValueError:
        print("Input Error!")
        n=input("Enter a number:")

print(n/2)
print(n)