def stateA(n):
    if(len(n)==0):
        print("string is  acc")
    elif(n[0]=='0'):
        stateA(n[1:])
    elif(n[0]=='1'):
        stateB(n[1:])
    else:
        print("string is not acc")
def stateB(n):
    if(len(n)==0):
        print("string is not acc")
    else:
        if(n[0]=='0'):
            stateA(n[1:])
        elif(n[0]=='1'):
            stateB(n[1:])
        else:
            print("string is not acc")
n=input("give a string in combination of 0 and 1 or decimal number divisible by 2:")
n=bin(int(n))[2:]
stateA(n)
    
    
        
    
