
def SumNonFact(value):

    sum=0
    for i in range(1,value,1):
        if((value%i)!=0):
            sum=sum+i
    return sum



def main():

    ret=0
    
    print("Enter the number")
    no=int(input())

    ret=SumNonFact(no)
    print(ret)


if __name__=="__main__":
    main()
