
def CountOdd(value):

    digit=0
    icnt=0
    

    while(value!=0):
        digit=value%10
        value=value//10
        if((digit%2)!=0):
            icnt=(icnt+1)
    return icnt



def main():

    ret=0
    
    print("Enter the number")
    no=int(input())

    ret=CountOdd(no)
    print(ret)

if __name__=="__main__":
    main()
