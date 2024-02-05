
# DICTIONARIES ARE STORED AS HASH TABLE IN MEMORIES

myDict={'name':'Tanmay','age':19}
print(myDict)
myDict['add']='ptk'
print(myDict)

def traverse(dictionaries):
    for keys in dictionaries:
        print(keys,dictionaries[keys])
traverse(myDict)

def search(dict,value):
    for keys in dict:
        if dict[keys]==value:
            return "found:" ,keys ,value
    return "value doesnt exist"
print(search(myDict,19))

# print(myDict.pop("age")) #RETURNS THE VALUE ONLY
# print("deleted dict",myDict)

# print(myDict.popitem()) # DELETES LAST ITEM AND RETURNS BOTH KEY AND VALUE
# print("deleted dict",myDict)

# myDict.clear()#DELETES ALL VALUES AND KEYS FROM A DICTIONARY
# print("deleted dict",myDict)

# del myDict #DELETES THE DICTIONARY ITSELF

copyDict=myDict.copy()
print(copyDict)

newDict={}.fromkeys([1,2,3,4],0) #IMPORTANT
print(newDict)

print(myDict.get('age',20))#WILL RETURN AGE VALE.. IF KEY ASKED IS NOT IN DICT, THEN IT WILL RETURN 2ND VALUE (HERE 20)
# print(myDict)