def Display(value):
    sum=0
    digit=0
    temp=value

    while(value!=0):
        digit=value%10
        sum=sum*10+digit
        value=value//10
    if(temp==sum):
        print("Palindrome")
    else:
        print("Not palindrome")




def main():

    print("Enter the number")
    no=int(input())


    Display(no)


if __name__=="__main__":
    main()

