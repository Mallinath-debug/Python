def Power(value,pow):

    i=0
    sum=1
    while(i<pow):
        sum=sum*pow
        i=i+1
    return sum



def main():

    print("Enter the number")
    no1=int(input())
    
    print("Enter the power")
    no2=int(input())

    ret=Power(no1,no2)
    print(ret)





if __name__=="__main__":
    main()
