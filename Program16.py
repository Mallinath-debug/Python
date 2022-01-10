

def FactDiff(value):
    fact=1
    sum=0
    sum1=0
    sum2=0
    for i in range(1,value,1):
        if((value%i)==0):
            sum=sum+i
            sum1=sum1+i
        else:
            return sum1-sum





def main():
    
    ret=0
    
    print("Enter the number")
    no=int(input())

    ret=FactDiff(no)
    print(ret)

if __name__=="__main__":
    main()
