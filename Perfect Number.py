# Perfect Number
# Perfect number is a positive number which sum of all positive divisors excluding that number id equal to  that number
# For example 6 is perfect number since divisor of 6 are 1,2 and 3
# Sum of its divisor is 1+2+3=6

def Display(value):

    i=1
    sum=0
    while(i<value):
        if((value%i)==0):
            sum=sum+i
            i=(i+1)
        elif(sum==value):
            return True
        else:
            return False




def main():
    
    bret=False

    print("Enter the number")    #will display this on screen
    no1=int(input())    #taking value from user

    bret=Display(no1)   #Function call

    if(bret==True):
        print("perfect Number")
    else:
        print("Not")





if __name__=="__main__":
    main()

