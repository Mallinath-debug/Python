
def MultFact(value):
    fact=1
    for i in range(1,value,1):
        if((value%i)==0):
            print(i)



def main():

    print("Enter the value")
    no=int(input())

    MultFact(no)


if __name__=="__main__":
    main()
