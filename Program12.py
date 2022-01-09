
def MultFact(value):
    fact=1
    for i in range(1,value,1):
        if((value%i)==0):
            fact=fact*i
    return fact



def main():

    ret=0
    
    print("Enter the value")
    no=int(input())

    ret=MultFact(no)
    print(ret)

if __name__=="__main__":
    main()
