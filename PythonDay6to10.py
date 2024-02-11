# Day 6 :-    ( variables and Data Types )

a = 5          # a is a varible and 5 is stored in memory location, the address where 5 is store is given a name 'a'.
print(a)
c = 3.0
b = "Harsh"
print(a)
print(str(a)+b)   # two similar Data Types can be added. so,first change the data types of a.
                  # addition of same type of Data Types is called CONCATENATION.
print(type(c))    # type function is used to know the type of Data Type.
d=type(a)
print(d)
print("The type of b is",type(b))
x=complex(8,2)
print(x,type(x))
print("the type of x is",type(x))

list1 = [7,2.3,[-4,6],{"name":"harsh","age":20},["apple","banana"]]
print(list1)     #list is mutable.

tuple1 = (("parrot","sparrow"),"lion","tiger")
print(tuple1)    # tuple is inmutable.

dict1 = {"name":"harsh","age":20}
print(dict1)
# Everything in python is object.

# Day 7:-   # ( Operators )

print(5+6)
print(15-6)
print(15*6)
print(2**3)  # means 2*2*2  ( multiplied 3 times )
print(15/6)  # used to division
print(15//6) # gives quotient ( // - floor division )
print(15%6)  # gives remainder ( % - modulus )

# Day 8 :-

# Day 9 :- ( type casting )

a="4"
b="3"
print(a+b)
print(int(a)+int(b))    # ( explicit typecasting )
x="Harsh"
y="Kumar"
print(x+y)
a=1
b=3
print(a+b)

# implicit typecasting ( automatic type change by python )
a=2.8                # float
b=3                  # integer
print(a+b)           # float

# Day 10 :- ( user input )

a = input("Enter your name:-")       # input():- function is used to take input from user.
print("my name is", a)

x= input("Enter your first number:-")
y= input("Enter your second number:-")
print(x+y)           # python takes input as string,so it combines as 522.if 1st no. is 52 and 2nd number is 2.

x= input("Enter your first number:-")
y= input("Enter your second number:-")
print(int(x)+int(y))    # so, we convert the datatype from string to int.

z=input("Enter desired number:-")
print(float(z))
