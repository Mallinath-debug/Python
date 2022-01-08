
def CheckEven(value):

    if ((value%2)==0):
        print("It is even number")
    else:
        print("It is odd number")


def main():


    print("Enter the number")
    no=int(input())

    CheckEven(no)


if __name__=="__main__":
    main()
