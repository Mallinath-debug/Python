#printing star

def Display(value):
    x=0
    while x<value:
        print('*')
        x=(x+1)


def main():

    print("Enter the number")
    no=int(input())

    Display(no)



if __name__=="__main__":
    main()
