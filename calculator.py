
while True:
    a=float(input("Enter 1st number: "))
    b=float(input("Enter 2nd number: "))
    k=input("Enter + - * / as per your needs")
    if k== '+' :
        sum=a+b
        print("The sum of two numbers is: ",sum)
    elif k=='-':
        sub=a-b
        print ("The difference of two numbers is: ",sub)
    elif k=='*':
        prod=a*b
        print("The product of two numbers is: ",prod)
    elif k=='/':
        div=a/b
        print("The remainder of two numbers is: ",div)



            