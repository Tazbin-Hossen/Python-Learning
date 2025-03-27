# using for loop in list 
numbers = [1,2,3,4,5]
ans = 0

for num in numbers :
    ans += num
print (ans)

# using range function to print (1-10)

sum = 0
for i in range (1,11) :
    print (i)

list5 = [10,20,30,40,50]
for i in range (len(list5)) :
    print ("index :",i+1, "expense : ",list5[i])

for i in range (1,6) :
    if(i%2 == 0) :
        {
            print ("for: ",i,"square is : ",i*i)
        }

# using while loop to print (1-5)

i = 1
while(i<=5) :
    print (i)
    i+=1


    
  
   