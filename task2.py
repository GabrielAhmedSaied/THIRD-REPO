#1.Create a simple function that takes 2 numbers and print their values
def variable(x,y):
    print(x+y)
variable(5,20)  
  
#######################################
# 2.In the above return function , use keyword arguments when calling the function  
variable(x=10,y=50)
#####################################
#3.In the above return function , give x and y default values of 0 and call the function with no arguments
def variable(x=0,y=0):
    print(x,y)
variable()  
#########################################
#4.Create a function that can take any number of arguments and print thesum of them
def sum (*items):
    add = 0
    for n in items :    
        add += n    
    print(add)          
sum(1,2,3,4)    
#4
def sun(n1=0,n2=0):
    return n1+n2
n=sum(5,6)
print(n)

#5.Create the same sum function using the lambda
sum=lambda n1,n2:  n1+n2
#6
print(sum(5,7))
##########################
#7 local is related with its own function but global is happened in all codes

