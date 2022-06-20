from audioop import add
from cgi import print_directory
from unicodedata import name
from winreg import KEY_ENUMERATE_SUB_KEYS


print("Exam Marks")
marks=38
if marks>=35:
    print("congrats!")
    print("you passed the exam!")

else:
    print("you failed the exam!")


#creating variables
name="sivakumar"
rollno=35
marks=38
print("Name:",name)
print("Roll:",rollno)
print("Marks:",marks)

#creating variables
a=b=c=90
print("a:",a)
print("b:",b)
print("c:",c)

#creating variables
a,b,c=70,80,90
print("a:",a)
print("b:",b)
print("c:",c)

#creating global variable
x=50
y=50
 
print("inside function sum=",x+y)

print("outside fucntion sum=",x+y) 

#Hello i am python
print("hello python")

X=5
y="shiva"
print(type(x))
print(type(y))

x="john"
print(x)
x='shiva'
print(x) 

a=5
A="shiva"
print(a)
print(A)

x,y,z = "orange","yellow","green"
print(x)
print(y)
print(z)

x=y=z = "green"
print(x)
print(y)
print(z)

fruits= ["apple","banana","mosambi"]
x,y,z= fruits
print(x)
print(y)
print(z)

x= "python is easy"
print(x)

x="python"
y="is"
z="not easy"
print(x,y,z)

x = str("Hello World")
print(x)
print(type(x)) 

Y = str("I am very healthy")
print(Y)
print(type(Y))

x = int(6)
print(x)
print(type(x)) 

Y = int(9)
print(Y)
print(type(Y))

x = float(45.5)
print(x)
print(type(x)) 

Y = float(80.5)
print(Y)
print(type(Y))

x = complex(2j)
print(x)
print(type(x)) 

Y = complex(1j)
print(Y)
print(type(Y))

x = list(("apple", "banana", "cherry"))
print(x)
print(type(x)) 

Y = list(("raj","kishan","avinash"))
print(Y)
print(type(Y))

x = tuple(("apple", "banana", "cherry"))
print(x)
print(type(x)) 

Y = tuple(("raj","kishan","avinash"))
print(Y)
print(type(Y))

X = range(2)
print(x)
print(type(x))

Y = range(20)
print(Y)
print(type(Y))

x = dict(name="John", age=36)
print(x)
print(type(x)) 

Y = dict(name="raghava", age=50)
print(Y)
print(type(Y))
a = "Hello, World!"
print(a[1])
a = "Hello python"
print(a[4])
a = "hello python"
print(a[0])
a = "hello raju"
print(a[7])
for x in "banana":
  print(x) 
for z in "desire":
  print(z) 
for y in "powershell":
    print(y)
for a in "terminal":
    print(a)
a = "Hello, World!"
print(len(a))
c = "Hello python"
print(len(c))   
b = "hello spaces you are bit difficult to understand"
print(len(b)) 
k = "hello 9102345666"
print(len(k))
txt = "The best things in life are free!"
print("free" in txt)
txt = "The best things in life are free!"
print("loss" in txt)
txt = "python is not easy"
print("is" in txt)
b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[5:8])
b = "hello python how are you?"
print(b[8:12])
b = "Hello, World!"
print(b[:5])
d = "master classes"
print(d[:9])
h = "hello temrinal b"
print(h[-8:-2])
o = "hello output"
print(o[-8:-3])
p = "my name is raj kumar"
print(p[-9:-6])
a = "Hello"
b = "World"
c = a + b
print(c)
a = "Hello"
b = " Python "
d = "how are you doing"
c = a + b + d
print(c)
a = "Hello"
b = "debug"
c = a + " " + b
print(c)
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
age = 49
txt = "my name is appparao, and i am {}"
print(txt.format(age))
age = 89
txt = "i am shiva and my age{}"
print(txt.format(age))
age = 97
txt = "my name is khan and my age is {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
quantity = 5
itemno = 345
price = 4500
myorder = "i want {} pieces of item {} for {} dollars"
print(myorder.format(quantity,itemno,price))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
txt = "we are the eArbor company from \"hHYDERABAD\" tech based company"
print(txt)
txt = 'It\'s alright.'
print(txt) 
txt = 'it\'s alright.You can come'
print(txt)
txt = "Hello\nWorld!"
print(txt)
txt = "hello\n I am shiva kumar"
print(txt)
txt = "hello\n keep down and up"
print(txt)
txt = "Hello\tWorld!"
print(txt) 
txt = "Hello\t kalyan!"
print(txt)
txt = "Hello \bWorld!"
print(txt)
txt = "hello \bpython i hope you are doing well!"
print(txt)
print(10 > 9)
print(10 == 9)
print(10 < 9)
print(19>9)
print(19 == 19)
print(25<29)
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")













