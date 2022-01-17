def CheckPrime(value):

    flag=False
    for i in range(2,value):
        if((value%i)==0):
            flag=True
            break
    if flag:
        print("NO")
    else:
        print("YES")



def main():

    print("Enter the number")
    no1=int(input())

    CheckPrime(no1)

if __name__=="__main__":
    main()

