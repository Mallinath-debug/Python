
def Factor(value):

    for i in range(2,value,1):
        if ((value%i)==0):
            print(i)



def main():

    print("Enter the number")
    no=int(input())

    Factor(no)

if __name__=="__main__":
    main()
