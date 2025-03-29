# dictionaries allows in python storing 'key value' pair 
phone_book = { "srijon" : 12345 , "soumen" : 78910 , "durjoy" : 112233}
print(phone_book)
print(phone_book["srijon"])  #accessing value(12345) using key("srijon")

phone_book["mamun"] = 22334455    #adding new key value in phone_book dictionary
print(phone_book) 
del phone_book["mamun"]    #delete a key value pair from the dictionary
print(phone_book)

#print a dictionary using for loop
for key in phone_book:
    print("key: ",key,"value: ",phone_book[key])

#print easily  
for k,v in phone_book.items():
    print(k,v)

# clear everything from dictionary using this function
phone_book.clear()
print(phone_book) 