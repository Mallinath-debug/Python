def CountRange(value):

    digit=0
    icnt=0

    while(value!=0):
        digit=value%10
        value=value//10
        if(digit>=3 and digit<=7):
            icnt=(icnt+1)
    return icnt



def main():

    print("Enter the number")
    no=int(input())

    ret=CountRange(no)
    print(ret)

if __name__=="__main__":
    main()