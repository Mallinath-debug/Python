
def Display(value1,value2):

    for i in range(0,value2,1):
        print(value1)

def main():

    print("Enter the first number")
    no1=int(input())

    print("Enter the second number")
    no2=int(input())

    Display(no1,no2)



if __name__=="__main__":
    main()
