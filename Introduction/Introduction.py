#Simple print statements
print 'Hello World !'
print '%s is number %d' % ("Python", 1)

#Variable assignment
myString = 'Hello World'
print myString

#Accept user input
user = raw_input('Enter user name \n')
print 'User name is: ', user

#Basic string
pystr = 'Python'
iscool = ' is cool!'
print pystr[0]
print iscool[1:3]
print iscool[4:]
print pystr + iscool
print pystr * 2

#Control statements
if 3 < 5:
    print 'true'
else: print 'false'

#List
aList = [1, 2, 3, 4]
print aList

#For
for item in ['e-mail', 'net-surfing', 'homework', 'chat']:
    print item

for item in ['e-mail', 'net-surfing', 'homework', 'chat']:
    print item,
print

for i in 'abc':
    print i

foo = 'abc'
for i in range(len(foo)):
    print foo[i], '(%d)' % i
