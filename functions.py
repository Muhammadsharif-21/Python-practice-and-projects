def gmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
    
def isgreater(a,b):
    if a>b:
        print("First number is bigger")  
    else:
        print("Second number is bigger")   
        
a = 9
b = 6
isgreater(a,b) 
gmean(a,b)   

c = 3 
d =10
isgreater(c,d)
gmean( c, d )


e=int(input("Enter values of e:"))
f=int(input("Enter values of f:"))

isgreater(e,f)
gmean(e,f)