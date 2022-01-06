#Division of two numbers

def Division(value1,value2):
    divide=0

    divide=value1//value2
    return divide

def main():

    print("Enter the first number")
    no1=int(input())

    print("Enter the second number")
    no2=int(input())

    ret=Division(no1,no2)
    print("Division is",ret)



if __name__ == "__main__":
    main()
