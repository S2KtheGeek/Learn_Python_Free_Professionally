#Code Reusability

def add(a, b): #formal arguments
    c = a + b
    print ('The sum is=',c)

def sub(a, b): #formal arguments
    c = a - b
    print ('The diff is=',c)

def mul(a, b): #formal arguments
    c = a * b
    print ('The product is=',c)

def div(a, b): #formal arguments
    c = a / b
    print ('The quotient is=',c)

def main():
    while True:
        i = int(input("If you want to continue press 0 else press any other number"))
        if i == 0:
            a = int(input("Enter a number"))
            b = int(input("Enter another number"))
            add(a,b)
            sub(a,b)
            mul(a,b)
            div(a,b)
        else:
            break

if __name__ == '__main__':
    main()
