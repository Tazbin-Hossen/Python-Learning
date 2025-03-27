# list mainly solve the problem stroing multiple varibles in one time
# important keyword we learned in this section 
# (append , insert , '+' , in , len) 

items = ["pasts","fruits","biscuits",65]
print (items)
print (items[0:2])       #slicing list from index '0' to before index '2'
print (items[-1])
items.append("drinks")   #added drinks in the end of list
print (items)
items.insert (1,"butter")
print (items)

fruites = ["mango","black berry","avocado"]
drinks = ["mojo","fanta","mirinda"]
items = fruites + drinks      #joining two list
print (items)
print (len(items))   #print the length of items
print ("apple" in items) 
print ("mango" in items)  # 'in' operator ensure that is "apple" is added in the list(items) or not . it returns boolean
