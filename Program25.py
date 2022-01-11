def MultDigits(value):
    
    digit=0
    fact=1

    while(value!=0):
        digit=value%10
        value=value//10
        fact=fact*digit
    return fact







def main():

    print("Enter the number")
    no=int(input())

    ret=MultDigits(no)
    print(ret)

if __name__=="__main__":
    main()
