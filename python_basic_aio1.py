print("Content that you wanna print on screen")   #recommended #double/single quote
print('Hi there');                                # ; not required
print('''I'm
             Susamay''')

Var1 = input('Who are you?  ')     #can't start with _ or number, can't contain $ &

print('Again! -> ') 
var1 = input()                     #alt scanf

print("It's nice talking to you"+ ''' ''' + Var1 + '\tSee Ya Later ' + var1)


# range(start, stop, step)
# start ->int optional (byDefault 0), stop -> int (not included), step ->int optional (byDefault 1)
for i in range(10): print(i)  
for i in range(10): print(i)  ; i = i+2; print(i)

# \n  \t   \\->\  \b->backspace  \ooo->Value_of_octalNumber \xhh->Value_of_hexNumber   
# \r -> will just work as you have shifted your cursor to the beginning of the string or line


variable_name2 = "String Data"
sliced_varName= variable_name2[1 : 6]   #index 1,2,3,4,5
print(sliced_varName) 

#string_variable.isalnum()    is_alPHABET_numERIC
print(variable_name2.isalnum())     #Returns True if ALL the characters in the string are alphaNumer1c, else False
                                   #space is not alphaNumeric

print(variable_name2.isdecimal())
print(variable_name2.isdigit())
print(variable_name2.islower())
print('isSpace =', variable_name2.isspace())    #use , instead of toString / str(#int_str)

print(id(variable_name2))   #memory_location_ofObject

print(sliced_varName.lower())    #converts toUpper
print(sliced_varName.upper())
print(variable_name2.strip())    #deletes leading & trailing SPACES
print(sliced_varName.capitalize())  #only First char of string will be Uppercase



'''4 built-in data types in Python used to store collections of data -> CSV
   LIST        []
   TUPLE       ()
   SET 
   DICTIONARY  {}                                                '''


list_example = []
myList = [ 9,2 ,5  ]      #any data type
print(myList[0])          #print element @ index 0

ZerothElementForList = myList.index(5)   #returns 5's index value
print(ZerothElementForList)

myList.append( 7  )     # $  These functions returns 'None' but, modifies myList  $
print(myList)                  #[9, 2, 5, 7]

myList.extend([0,5,7,0])       #extends by another LIST or ITERABLE
print(myList)                  #[9, 2, 5, 7, 0, 5, 7, 0]
myList.insert(1, 14)    #index_position, element
# myList = myList.insert(1, 14)   # this is wrong
# print(type(myList))             # <class 'NoneType'>
myList.pop(2)           #Removes at index 2
print('after pop', myList)                  #[9, 14, 5, 7, 0, 5, 7, 0]
myList.remove(0)        #Removes first occurance
list_example.clear()    #Removes all the elements
print(myList.count(5))  #no of occurance of 5
myList.reverse()        #Returns reverse of a list
print(myList)

# print(list.sort(reverse=True|False))
myList.sort(reverse=False)  #Sorts the list, True For decending & False for accending
print(myList)

myMixList = [14201617025, "Susamay" , 8.14 ]
print(myMixList)


#Tuples are represented as comma-separated values of any data type within ()
#Once declared, cannot be changed; is memory efficient & faster than list
#variable_name = (element1, element2, ...)

tupleMix = ("Susamay", "Kumbhakar", 22, True, 'infosys')
print(tupleMix)
myTuple = (10 , 11 , 1, 17,1 , 1, 1, 10)
print(myTuple)
myTuple.index(17)                #index position of element=17
myTuple.count(1)                 #number of occurance for 1


#Set {} -> collection of multiple values which is unordered & unindexed    
         # unchangable -> cannot change its items, but you can remove items and add new items.
# var_name = {element1, element2, ...}       OR
# var_name = set([element1, element2, ...])

mySetMix = {"Susamay", 9830909908, 'susamay.sk@gmail.com'}
mySet = {2, 10, 500, 2, 2, 10}
mySet.add(4)       #adds element to last position
mySet.discard(2)     #removes all occurance of 2
print(mySet)

print(mySet.intersection(mySetMix))   #returns common elements

set1 = {55, 33, 33, 0, 1}
set2 = {33, 0,0, 65, 0}
set3 = {33, 55, 0, 1, 1 }
set4 = {33, 0,0, 65, 0, 66}
print(set1.intersection(set2, set4, set3))  #returns common elements
print(set2.issubset(set4))                  #set4 is subset of set2 ?

mySet.pop()                #removes item from START
print(mySet)
set4.remove(0)             #removes all occurance of 0 from set
print(set4)

set4.union(set1, set3)     #Returns the union of two or more sets
print(set4)
mySet.clear()              #empties a set

#Dictionaries -> ordered (from python 3.7) {key:value} pair &  no two KEYS can be the same 
# myDict = {key: value, key: value, ...}

thisDict = {"brand": "Ford",  "electric": False,  "year": 1964,
            "colors": ["red", "white", "blue"]}

myDictSquare = {1:1, 2:4, 3:9, -3:9, 4:16 }
                           #Adding Element
myDictSquare[-4] = 16      #If that key already exists, then its value will get updated
del myDictSquare [2]
print(myDictSquare)
print(len(myDictSquare))   #length

squareOfMinus4 = myDictSquare.get(-4)  #returns value for key -4
print(squareOfMinus4)

print(myDictSquare.items())            #returns tuple of each pair
print(myDictSquare.keys())
print(myDictSquare.values())

myDictSquare2 = {-9:81, 0:0}
myDictSquare.update(myDictSquare2)     #adds another dictonary / iterable-pair
print(myDictSquare)
thisDict.clear()         #empties a dictonary



# CONDITIONAL STATEMENTS

gravity = 1.62      #earth ->9.81
gravity = 9.81 


if (gravity == 9.81)  :  print('you are on earth')
elif (gravity == 1.62) : print('you are on moon')     #multiple elif possible
else : print('where are you Mr. astronaut?')          #optional

#0 is False, rest are True
if(gravity)  : print('Hi')


items = [10, 0 , 1 , 1 , 20]
for item in items : item+1; print(item)

# LOOP

sum_Now, iterator = 0, 0
for iterator in range(10): 
   sum_Now = sum_Now + iterator   
   print(sum_Now)                #the whole statment will repeat with iterator

      #while(boolean==True) : loop this body    #break -> brakes control out of the loop
while(gravity != 9.81 or gravity != 1.62) : print('measured gravity is ' +  str(gravity)); break;
print(   type(gravity)  )     #returns datatype #str(gravity)-> like toString method

      #continue -> skips the rest of the loop statements and continues with NEXT ITERATION



#Function is a block of code that performs a specific task

def fun(): print("Hi there!")       #function definition
fun()                               #function call

'''             def function_name(parameter1, ...):
                body of the function
                return expression         
                        OR
                def function_name(parameter: data_type, ...) -> return_datatype:
                body of the function
                return expression
                
                                                   '''

# *args -> arbitary arguments
# **kwargs -> arbitary keyword arguments


#FILE HANDLING
'''
var_name = open("file name", "mode")  ->r/w/a/r+/w+/a+
                          ->  a+: To append and read data from the file. It wont override existing data.
                      r+:  To read and write data into the file. The previous data in the file will be overridden.
var_name.close()
read() #return one big string
readlines() #returns a list
readline #returns one line at a time
write() #Used to write a fixed sequence of characters to a file
writelines() # used to write a list of strings

file = open("Hello.txt", "a")    #a = append
'''

fileC = open("random.txt", 'r+')
# for each_char in fileC: print (each_char)   #print data
fileC.write("\n execution complete")
# for each_char in fileC: print (each_char)   #print data
print (fileC.read(100))             #first 5 char , if 
fileC.close()

# fileC = open("random.txt", "r")


#Exception Handling  -> try and except (like try-catch block) , finally is optional
unassignedValue = 7
try:
  print(unassignedValue = 1)
except:                    #multiple except allowed when finally is absent
  print("An exception occurred: Define the value of unassignedValue")
# except:                 
#    print("This will not get executed as previous EXCEPT already executed")
# else:
#    print("nothing went ")
                           #else keyword CAN be used to be executed if TRY is EXECUTED SUCCESSFULLY
finally: 
   print("Exception Handled Successfully")


# JL = 5                    #-->complex
# try:
#     JL<6
#     raise Exception()
# except Exception as e2:
#     print('error handled')                      #[Error processing block]



x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")     #TypeError/Exception



#Object Oriented Programming (OOPS)
'''         SYNTAX      
      class class_name:
      pass #statements           '''

class Dog:
 
    # class attribute
    attr1 = "mammal"
 
    # Instance attribute    
    def __init__(self, name):     #__init__ is constructor (initialize the instance variable, automatically executed when object created)
        self.name = name
                                  #method are used to do operations/actions (like printing data members), we should explicitly call & can be of any name
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
 
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
 
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

