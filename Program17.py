
def DisplayDigit(value):
    idigit=0

    while(value!=0):
        idigit=value%10
        print(idigit)
        value=value//10

def main():

    print("Enter the number")
    no=int(input())

    DisplayDigit(no)


if __name__=="__main__":
    main()
