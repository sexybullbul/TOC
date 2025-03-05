def stateA(n):
    if(len(n)==0):
        print("string is not acc")
    elif(n[0]=='0'):
        stateA(n[1:])
    elif(n[0]=='1'):
        stateB(n[1:])
def stateB(n):
    if(len(n)==0):
        print("string is not acc")
    else:
        if(n[0]=='0'):
            stateC(n[1:])
        elif(n[0]=='1'):
            stateB(n[1:])
def stateC(n):
    if (len(n)==0):
        print("string is not acc")
    else:
        if(n[0]=='0'):
            stateA(n[1:])
        elif(n[0]=='1'):
            stateD(n[1:])
def stateD(n):
    if (len(n)==0):
        print("string is  acc")
    else:
        if(n[0]=='0'):
            stateC(n[1:])
        elif(n[0]=='1'):
            stateB(n[1:])
n=input("give a string in combination of 0 and 1:")
stateA(n)
    
    
        
    
