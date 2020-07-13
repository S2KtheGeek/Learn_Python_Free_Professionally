'''Hello guys in todays session we will primarily learn about the following things
1. More on DataTypes
2. List
3. Tuples
4. Set
5. Dictionaries
6. Range
7. Loops - For and while
'''

#More on DataTypes
a = None
if a is None:
    print ('None value')
else:
    print('Value Exists')

b = 5
f = 6.3
c = 3 + 5.3j
print(b, ' ', c, ' ', f)
print(type(b), ' ', type(c), ' ', type(f))

bo = 10 > 5
print(bo, 'Type of=', type(bo))

#SET in python
s ={10, 20, 30, 40}
print(s)
s1={10, 20, 40, 50, 20, 20, 10}
print(s1)

#Strings Basics
s1 = "STG_Youtube"
s2 = 'stg_YouTube'
print(s1, '\n', s2)

'''Say for a case you need to embed a string in a string, the we use ''' ''' quotes '''
st = '''My name is 'Subhra'. I am your host'''
print(st)

print(st[1])

#print(st[3:7])

#print(st[-1])

#List the most powerful Data Structure in python
l1 = [10 , 20, 'a', 'STG', True]
print(l1)
#Finding length of list
print (len(l1))
#Always remember index starts at 0 and ends at len(lt)-1
#accessing element of the list
print(l1[2])
#List Slicing-Getting the second element to 4th element
print(l1[1:4])#here the first number is taken as the index and it goes to one index less than the last number, with a default step size of 1
#With A given step size
print(l1[1:4:2])
#get the last element of the list
print(l1[-1]) #Similar to print(l1[len(l1)-1])

l = []
print(l)
l11 = [1]
print(l11)

#The range function - range()
#Syntax  range(start, stop, stepsize) Default stepsize = 1
lst = range(0, 10)
print(lst)
print(type(lst))

#Convering A range to list
lst = list(lst)

print (lst)

#Updating elements of the list
lst[3] = 40
print(lst)
#updating multiple elements of the list i.e parts and not individual indexes
lst[3:5] = 23, 45
print(lst)
#lst[3, 5, 7] = 40, 23, 56 3 This is wrong
#printing the list in reverse order

lst.reverse()
print(lst)
print(type(lst))

#Using a list as stack
print(lst)
#push operation on list
lst.append(25)
print(lst)
#Pop Operation on List
print(lst.pop())
print(lst)

#Concatenation of two lists or more than 2 lists
print(l1)
l3 = l1 + lst
print(l3)
l4 = list(range(45,75,10))
print(l4)
l5 = l4 + lst
print(l5)

#Check whether an element is present in the list or not
print(45 in l5)

#sort the members of the list
print(l5)
l5.sort()
print("In Ascending order:",l5)
l5.sort(reverse=True)
print("In Descending order:",l5)

#Repetation of list
print(l3)
print(l3*3)#prints the list 3 times
#Minimum and maximum of a list
print(l5)
print('Minimum in the list=', min(l5))
print('Maximum in the list=', max(l5))

#Multidimenstional List
ml = [[[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]]
print(ml)



#Tuples in python
t = ()
print(t)
t1 = (1, )
print(t1)
t2 = (10, 20, -3, 4.5, 'STG', 'YouTube')
print(t2)

#Accessing elements of the tuple
print(t2[2])
print(t2[-1])

#Tuples are immutable, while lists are multable
print(t2)
#t2[3] = 5
print(t2)

#max min and len are supported by tuples too.

#Dictionaries
dict = {'Name': 'STG', 'ID': 1234, 'YouTube': True, 'Salary': 0.1}
print(dict)

#there are many more methods in the list, tuples and dictionary which will be discussed while discussing them in details



#For Loop
sumf = 0
for k in range(1,11):
    sumf = sumf + k
print (sumf)

#For with else
sumf = 0
for k in range(0,10):
    sumf = sumf + k
else:
    print("Condition over")
print (sumf)

#For with lists
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sumk = 0
# iterate over the list
for val in numbers:
	sumk = sumk + val

print("The sum is", sumk)

#For as index
genre = ['pop', 'rock', 'jazz']
for i in range(len(genre)):
	print("I like", genre[i])

#For on tuples
T = (10,20,30,40,50)
for var in T:
    print (var)

#for on dictionaries
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key, '->', a_dict[key])


#This will be more than most of the things you would require for basic python. The other things will be discussed in the detailed discussions of each after these 7 days
