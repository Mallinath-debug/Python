def Fibonacci(value):
    n1=0
    n2=1
    count=0
    print("Fibonacci series is")
    while(count<value):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1

def main():

    print("enter the range")
    no=int(input())

    Fibonacci(no)

if __name__=="__main__":
    main()
