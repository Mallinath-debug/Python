def Reverse(value):
    digit=0
    while(value!=0):
        digit=value%10
        print(digit)
        value=value//10

def main():

    print("Enter the number")
    no=int(input())

    Reverse(no)



if __name__=="__main__":
    main()
