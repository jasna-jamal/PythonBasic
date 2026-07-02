while True:
    a=int(input("Enter First No:"))
    b=int(input("Enter Second No:"))
    print("Choose an Option")
    print("A:Sum")
    print("B:Diiference")
    print("C:Product")
    print("D:Division")
    print("E:Modulo")
    print("F:Floor division")
    print("G:exponentiation")
    op=input("Enter the operation:")
    if op=='A':
        print("SUM =",a+b)
    elif op=='B':
        print("Difference=",a-b)
    elif op=='C':
        print("Product=",a*b)
    elif op=='D':
        print("Quotient=",a/b)
    elif op=='E':
        print("Remainder=",a%b)
    elif op=='F':
        print("Floor division=",a//b)
    elif op=='G':
        print("Exponent=",a**b)
    else:
        print("WRONG INPUT!!!")
