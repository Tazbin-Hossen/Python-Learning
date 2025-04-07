data = open("demo.txt","r")
ans = data.read()
print(ans)
data.close()

              #-----------file modules------------#
# 'r' = open for reading
# 'w' = open for writing,truncating the file first
# 'x' = creat a new file and open it for writing 
# 'a' = open for writing and append a file at end of the file if it is exist
# 'b' = binary mode
# 't' = text mode
# '+' = open a disk file for updating (reading and writing)

          #---------reading a file-------------#

f = open("demo.txt","r")
data1 = f.readline()
data2 = f.readline()
print(data1.rstrip())
print(data2.rstrip())
f.close()

         #----------writing to a file-----------#

f2 = open("demo.txt","w")
data3 = f2.write("This is a new line.") #overwrites the file
f2.close()

f3 = open("demo.txt","a")
data4 = f3.write("This is another new line.") #adds in the end
f3.close()

#important links from stackoverflow to learning more about modes
#https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function
 
            #---------delete a file-------------#

# import os
# os.remove("demo.txt")