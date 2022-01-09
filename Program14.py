

def FactRev(value):

    ifact=1
    for i in range(1,value,1):
        if((value%i)!=0):
            print(i)


def main():

    print("Enter the number")
    no=int(input())

    FactRev(no)

if __name__=="__main__":
    main()
