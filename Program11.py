
def DisplayEven(value):

    for i in range(2,value,2):
        if((value%i)==0):
            print(i)




def main():

    print("Enter the number")
    no=int(input())

    DisplayEven(no)


if __name__=="__main__":
    main()
