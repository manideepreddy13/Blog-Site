# a start
print("Hello World!")

# python interpretor reads a number and interprets it as an int or a float
a = 5.21

print(a+4)

# paragraph print
span = '''Que
Que
Mira
Mira'''

print(span)

# list and item
lst = ['a', 'e', 'i', 'o', 'u']

print(lst[0])

# tuple - unchangable

who = ('me', 'myself', 'i')
print(who)

# dictionary - maps from keys to values

dict = {'name': 'manideep', 'age': '19', 'place': 'thikkodi'}
print(dict['place'])


# STRING OPERATION
# concatenation
print('i'+' am')

# replication
print('knight '*10)

# upper and lower capital
nm = 'list'
print(nm.upper())

# formatter

stri = "i am not going to give {}"

print(str.format('up'))


stri = '{1} eats {0}'

print(str.format('veg', 'he'))

# type specifier

string = 'he finished {0:f} of the work'

print(string.format(75))


# power

x = 3

print(float(x**x))


# if else statements

grade = 75

if grade > 80:
    print("A")

elif (grade < 80 and grade > 70):
    print('B')


# while loop
stri = '''
x = int(input())

lst = [0]

while x>0:
    lst.append(x)
    print(lst)
    x = x-1
'''

# for loop

inti = []

for i in range(8):
    l = str(i)
    inti.append(l)
    print(inti)

# for loop in 2D list
list_of_lists = [['hammerhead', 'great white',
                  'dogfish'], [0, 1, 2], [9.9, 8.8, 7.7]]

it = []

for list in list_of_lists:
    for item in list:
        it.append(item)

    print(it)
    it = []


# function

def addnumbers(a, b, c):
    return a+b+c


print(addnumbers(1, 2, 3))
