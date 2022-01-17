def FactorialX(value):
    fact=1
    for i in range(1,value+1):
        fact=fact*i
    return fact


def main():
    
    

    print("Enter the number")
    no=int(input())

    ret=FactorialX(no)
    print("Factorial is ",ret)

if __name__=="__main__":
    main()
