list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]

num = input("enter a num : ")
num = int(num)

if(num in list1) :
    {
        print ("number in list 1.")
    }
elif (num in list2) :
    {
        print ("number in list 2.")
    }
else :
    {
        print ("number in list 3.")
    }