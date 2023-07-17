
#Default functions

'''
def sample(fname , lname="Mark",standard = "Fifth"):
    print(fname,lname,"studies in ",standard,"class")


sample("Gautham")

'''

#List functions

'''
def appenditems(itemName,itemList = []):
    itemList.append(itemName)
    return itemList


appenditems('a')
print(appenditems('ab'))

'''

#Dict Func

'''
def additemtodict(itemName,quan,itemList={}):
    itemList[itemName] = quan
    return itemList

additemtodict("a",1)
print(additemtodict("ab",2))

'''



'''

# using None as values of the default arguments

print('#list')

def appendItem(itemName, itemList=None):
	if itemList == None:
		itemList = []
	itemList.append(itemName)
	return itemList


print(appendItem('notebook'))
print(appendItem('pencil'))
print(appendItem('eraser'))


# using None as value of default parameter

print('\n\n#dictionary')
def addItemToDictionary(itemName, quantity, itemList = None):
	if itemList == None:
		itemList = {}
	itemList[itemName] = quantity
	return itemList


print(addItemToDictionary('notebook', 4))
print(addItemToDictionary('pencil', 1))
print(addItemToDictionary('eraser', 1))


'''


'''

#Multiple Returns

def split_name(name):
	first_name, last_name = name.split()
	return first_name, last_name

f_name, l_name = split_name("John Doe")
print("First Name:", f_name)
print("Last Name:", l_name)


'''







