'''
# Wap to code a function where it will not take any parameter and not
#return any value
r = float(input("Enter Radius:  "))

def ar_circle():
    ar = 3.14 *r*r
    print("Area of circle:  " , ar)
    
ar_circle()
'''
'''




# Wap to code a function where it will  take any parameter and not
#return any value
r = float(input("Enter Radius:  "))

def ar_circle(radius): # formal variable  # function defination ,
                      #r is a parameter
    ar = 3.14 *radius*radius
    print("Area of circle:  " , ar)
    
ar_circle(r)  #Actual variable# function calling  , r is parameter
'''

# Wap to code a function where it will  take any parameter and 
#return specific value
'''
r = int(input("Enter Radius:  "))

def ar_circle(radius): # formal variable  # function defination ,
                      #r is a parameter
    ar = 3.14 *radius*radius
    return ar
  
    
#print(ar_circle(r))  #Actual variable# function calling  ,
                       #r is parameter
s = ar_circle(r)
#print("ans: " , int(s))
print(s)
'''
'''
# wap to return the multiple values with the
# define function name it to_calc()

def to_calc(x,y):
    return x+y , x-y , x*y , x/y

p = int(input("Enter p:  "))
q = int(input("Enter q:  "))

add , sub , mul , div= to_calc(p , q)
print("add:  " , add , "  sub: " , sub)
print("mul:  " ,mul , "  div: " , div)
'''

'''
# wap to calculate the sum of three numbers
# and pass the sum into another function which
#will return the average of returned value

def func1(x , y , z):
    return x+y+z

def func2_average(q):
    return q/3

t = func1(10 , 30 , 20)
print("Sum of number:  " , t)

m = func2_average(t)
print("Average of number:  " , m)
'''
'''
def func(sanjana):  # formal
    print("before defination statement: " ,num )
   
    sanjana = sanjana+1       # a , num  scope :  local , 
    print("inside function: " , sanjana) #5

num=4
print("before calling " , num)
func(num)  # actual    # num scope: global
print("after calling " , sanjana)'''

'''
john=None
def greet():
    john=223.5655
    print("Hello" , john) # noscope is define of john

greet()
print(john)

'''

# scope of functions
'''

def greet():  # scope of defination global
    print("I am Happy ")
    def bye():   # defination local
        print("Hmm bye byee:  ")
        
        
    bye() # scope local


greet()  # scope of function calling is global
#bye()    # scope global but not able to access
             # bcz deination available in another function

'''
#  Types of Arguments
#(1. positional 2. Default 3. Keyword Argument
'''
# wap to demonstrate the use of positional argument

def p_arg(x , y , z):
    return(x*y-z)

a=10
b=20
c=30

print(p_arg(a , b , c))

'''

# wap to demonstrate the default argument

'''
def si(principle=100 , time=0, rate=0.5):
    return (principle * time * rate)/100

print(si( 100, 10))


# 2*10*0.5/100 = 0.1
#100*2*10/100 = 20

#100*10*0.5/100 =5
'''


'''
# wap to demontrate the keyword argument


def student(name="Govinda" , rollno=33):
    print("Name:  " , name)
    print("rollno:  " , rollno)


#student('alok nath' , 25)
#student(rollno=25 , name='sarika')
student( rollno=100, name="Herman")

'''

'''
# Wap to pass mutable data type into the function
# by passing list
mylist = [2 , 3 ,4 ,5 ,6,7] # global

def my_func(mylist):
    gov = [11 , 12 , 13 , 14 , 15]    # defining of function
    mylist.extend(gov)
    print(mylist)      # formal parameter

print("before calling: " , mylist)    
my_func(mylist)  # calling of function/Actual
print("after calling: " , mylist)   # parameter
'''
'''
# passing an immutable type value
a = 3
def func(a):
    print("inside 'a' value : " , a)
    a = a + 2
    print("inside 'a' value after changing : " , a) 

print("Before calling :"   , a)
func(a)
print("afer calling :"   , a)

'''


#LEGB Rule:  local-Enclosing-Global-Builin


'''
x=100  # global

def outer():
    y=200    #   enclosing variable
    def inner():
        x=50      # local variable
        print(x)
    inner()

outer()

'''
# Demonstration of LEGB rule

from math import pi
#print(pi)

x = pi   # global variable   # LEGB
def outer():
   # pi = 2.14  # eclosing variable 
    def inner():
        #nonlocal pi
       # print("we are using enclosing variable as nonlocal: " , pi)
       # h = pi  + 2
       # print(h)
        ## global pi
        #pi = pi + 1
       # pi = 1.14    #  local variable
       # print("inside pi:  " , pi)
    inner()
    
outer()
print(pi)

#print("after calling:  " , pi)















































    























































    