# display number in reverse order

def Reverse(value):
    for i in range(value,0,-1):
        print(i)

def main():

    print("Enter the number")
    no=int(input())

    Reverse(no)


if __name__=="__main__":
    main()
