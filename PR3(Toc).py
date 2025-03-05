#1
#Generate a sequence of  string

#write a python program to  generate a string over {0,1,2,3,........9}when given string is IDID.
def StringMatch(s):
    lo,hi=0,len(s)
    ans=[]
    for x in s:
        if x=='I55':
            ans.append(lo)
            lo+=1
        else:
            ans.append(hi)
            hi-=1
    return ans + [lo]
s="IDID"
print(StringMatch(s))

#2
#create program to generate a random string using the random.choice() function
import string
import random
s=10
#call random.choices()string module to find the string in Uppercase + numeric data
ran="".join(random.choices(string.ascii_uppercase+string.digits,k=s))
print("The randomly generated string is:"+str(ran))

#3
#write a program to generate the  random string in uppercase & lowercase letter
import random
import string
def Upper_Lower_string(length):
    result="".join((random.choice(string.ascii_lowercase)for x in range(length)))
    print("Random string generated in Lowercase: ",result)
    result1="".join((random.choice(string.ascii_uppercase)for x in range(length)))
    print("Random string generated in Uppercase: ",result1)
Upper_Lower_string(10)
