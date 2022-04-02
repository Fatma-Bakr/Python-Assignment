##Assignment Ques#1 	Find the nth Occurrence of a word in a string!

def find_nth_occurrence(substring, string, occurrence=1
                       ): 
    fnd=string.find(substring,0,len(string)) 
    if occurrence==1: 
        return fnd 
    else: 
        while occurrence>1: 
            fnd=string.find(substring,fnd+1,len(string)) 
            occurrence-=1 
            return fnd 
        
substring=input('Substring u r looking for : ')
string=input('String U r looking in : ')
occurrence=int(input('Please Enter the number of the occurrence : '))
print(find_nth_occurrence(substring, string, occurrence))

##Assignment Ques#2 	Simple String Matching

def solve(a,b):
    if a==b and '*' not in a:
        return True 
    elif a=='*' or a=='': 
        return True
    elif '*' in a and ((len(b))<((len(a)-1))):
        return False 
    elif '*' in a and ((len(b))>=((len(a)-1))): 
        for i in range((len(a)+1)): 
            if a[i]==b[i]: 
                return True
            elif a[i]=='*': 
                break
            else: 
                return False 
        for j in range(-1,-(len(a)+1),-1):
            if a[j]==b[j]: 
                return True 
            elif a[j]=='*': 
                break 
            else: 
                return False 
    else: 
        return False

a=input('Please Enter String a : ')
b=input('Please Enter String b : ')
print(solve(a,b))

##Assignment Ques#3 	Is it a palindrome?

def is_palindrome(s):
    s1=s[::-1]
    s_upper=s.upper()
    s1_upper=s1.upper()
    return s_upper==s1_upper

s=input('Please Enter A String : ')
print(is_palindrome(s))

##Assignment Ques#4 	Repeated Substring (Bonus Question)

def f(s):
    t=''
    k=0 
    for i in range(len(s)):
        t+=s[i]
        k=s.count(t) 
        if t*k==s:
            return (t,k)
    return(s,1)
s=input('Please Enter A String : ')
print(f(s))

