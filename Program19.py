
def CheckZero(value):
    idigit=0
    icnt=0

    while(value!=0):
        idigit=value%10
        value=value//10
        if(idigit==2):
            icnt=(icnt+1)
    return icnt

def main():
    
    

    print("Enter the number")
    no=int(input())

    ret=CheckZero(no)
    print(ret)


if __name__=="__main__":
    main()
