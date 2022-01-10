
def CheckZero(value):
    digit=0

    while(value!=0):
        digit=value%10
        value=value//10
        if(digit==0):
            return True
        else:
            return False

def main():

    bret=False
    print("Enter the number")
    no=int(input())

    bret=CheckZero(no)
    if(bret==True):
        print("IT HAS ZERO")
    else:
        print("IT HAS NO ZERO")

if __name__=="__main__":
    main()
