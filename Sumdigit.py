def Reverse(value):
    digit=0
    sum=0
    while(value!=0):
        digit=value%10
        sum=sum+digit
        value=value//10
    return sum

def main():

    print("Enter the number")
    no=int(input())

    ret=Reverse(no)
    print(ret)



if __name__=="__main__":
    main()
