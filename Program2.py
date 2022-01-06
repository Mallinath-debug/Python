#Printing *,Anything on the screen by taking number

def Display(value):
    for i in range(0,value,1):
        print("Marevllous")

def main():
    no=0

    print("Enter the size")
    no=int(input())

    Display(no)


if __name__=="__main__":
    main()
