# Python Day 11 :- ( String)

name="Harsh"
Friend="Lalit"
print("Hello,",Friend)
print("Hello"+name)     # string may be inside double or single quotes.
apple='He said,"I want to eat an apple."'
print(apple)
apple1="He said,\"I want to eat an apple.\""
print(apple1)

# MULTIPLELINE STRING :-
# '''     '''' is used for multiple string.
mango='''He said,
Hi Harsh,
How are you ?
"Would you like to eat Banana"'''
print(mango)
print(name[0])    # this is called indexing.it's start from 0.
print(name[1])
print(name[2])
print(name[3])
print(name[4])
#print(name[5])   # it gives index errror,because no more character in string.

# for loop in string :-
for character in mango:        # this code gives all character of string at a time.
    print(character)

a="A,B C,~"         # comma,symbol or space all are counted in indexing.
print(a[0])         # index of 1st letter of string is 0.
print(a[1])
print(a[3])
print(a[6])

# Python Day 12 :- (string slicing)

name1="Pritam,Raj"     # for slicing square braces are used.
print(name1[2:7])      # 2 is starting index of character from you want string slicing and 7(6+1) is last character till you want to string slicing.
                       # string slicing will take upto 6 if you give 7.
print(len(name1))

fruit = "mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4])      # including 0 but not 4.
print(fruit[1:4])
print(fruit[:5])            # print(fruit[0:5]) is equivalent to print(fruit[:5])
print(fruit[:])             # print(fruit[:])  is equal to print(fruit[0:last] )

# NEGATIVE SlICING :-

print(fruit[:-3])          # print(fruit[0:len(fruit)-3])
print(fruit[0:len(fruit)-3])
print(fruit[-1:len(fruit)-3])     # print(fruit[len(fruit)-1:len(fruit)-3]), it means 4:2 (no sense). NOTHING WILL BE PRINTED.
# in negative slicing python automatically add len(fruit).
print(fruit[-3:-1])         # print(fruit[len(fruit)-3:len(fruit)-1]), it means 2:4 ( NG WILL BE PRINTED )

# QUICK QUIZ :-
nm="Harsh"
print(nm[-4:-2])










