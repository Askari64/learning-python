import random

a, b = 29, 43
def sum(a , b): 
    summed = a + b
    print(summed)

def compare():
    if a > b :
        print(str(a) + " is greater than " + str(b))
    else:
        print(str(b) + " is greater than " + str(a))

name = "Askari"

def greet():
    print(f"Hello {name}")

def randomNumber():
   print(random.randrange(1,100))

def loopString():
    varString = "Blue"
    for x in varString:
        print(x)
    print(f'Length of {varString} is {len(varString)}')

def joinLists():
    list1 = ['a', 'b', 'c']
    list2 = [1, 2, 3, 4]
    list3 = list1 + list2
    ###################################
    #list1.extend(list2) works the same
    #for x in list2:
      #list1.append(x)
    ###################################
    print(f'Length of {list3} is {len(list3)}')

def inTuple():
    fruitsTuple = ("apple", "banana","mango","orange")
    if "apple" in fruitsTuple:
        print("Apple is in fruit tuple")

def pythonSetFn():
    pythonSet = {"apple", "banana", "pear", 1, True} # True and 1 are considered duplicates for set
    pythonSet.add("tomato")
    tropical = {"Pineapple", "Mango", "Papaya"}
    pythonSet.update(tropical)
    pythonSet.discard("banana") # .remove() works same but it throw error unlike discard
    print(pythonSet)

def carDict():
    myCar = {
        "Brand": "Lamborghini",
        "Model": "Gallardo",
        "Year": 2003
    }

    print(myCar["Brand"])
    myCar.update({"Model": "Huracan"})
    print(myCar.items())

def recursionFactorial(n):
    #base case
    if n <= 1:
        return 1
    #recursive case
    else:
        return n * recursionFactorial(n - 1)

def main():
    sum(567,34)
    compare()
    greet()
    randomNumber()
    loopString()
    joinLists()
    inTuple()
    pythonSetFn()
    carDict()
    print(recursionFactorial(5))

main()

"""
List Methods

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

Tuple methods

count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found

Set Methods

add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others

Dictionary Methods

clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

"""
