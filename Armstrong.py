# Armstrong Number
# Those number whose sum of cube of its digit is equal to that nuber are known as Armstrong Number
# For Example 153 (1^3)+(1^5)+(1^3)=1+125+9=153
# Armstrong number are 370,371,407
# Those numbers which sum of its digit to power of number of its digit is equal to that number are known as Armstrong Number
# Example : 1634
# total Digits is 4
# (1^4)+(1^6)+(1^3)+(1^4)=1+1296+81+64=1634

def Display(value):
    temp=value
    digit=0
    sum=0

    while(value!=0):
        digit=value%10
        sum=sum+(digit*digit*digit)
        value=value//10
    if(sum==temp):
        print("YES")
    else:
        print("NO")



def main():

    print("Enter the number")
    no1=int(input())

    Display(no1)




if __name__=="__main__":
    main()

