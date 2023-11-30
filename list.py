
# #---> LIST <--- [ ]
# allows duplicate 
# any type of data can be stored
# we can modify list item
# # append - direct
# # extend
# # insert - index
# # remove - direct
# # delete - index
# # clear
# # sort
# # reverse
# # copy
# # pop
# # count
# # check if exist
# # len - length

# # a=[1,2,3,4,5]
# # sum=0
# # for i in a:
# #     sum = sum+i
# # print(sum)


# #List operations :
# # it supports diffrent data types:
# # list1 = [1,"hello",3.4]
# # print(list1)
# # for i in list1:
# #     print(i)
    
# # accessing - 
# languages = ["python","java","javascript"]
# print(languages[0])    
    
# # negative index - 
# print(languages[-1])

# #slicing of list - 
# letters = ['p','y','t','h','o','n']
# print(letters[2:4])
# print(letters[:])

# #append - 
# languages.append("django")
# print(languages)

# #extend - 
# numbers = [1,2,3]
# num = [4,5,6]
# numbers.extend(num)
# print(numbers)

# #insert - 
# numbers.insert(3,31)
# print(numbers)

# #delete - 
# del numbers[3]
# print(numbers)
# del numbers[0:2]
# print(numbers)

# #remove - 
# numbers.remove(5)
# print(numbers)

# #reverse - 
# languages.reverse()
# print(languages)

# #clear - 
# numbers.clear()
# print(numbers)

# #check if an element exist in a list
# print('C' in languages)

# #length - 
# print(len(languages))


# a=[]
# for i in range(10):
#     sum=int(input())
#     if sum%2==0:
#       a.append(sum)
    
# add=0
# for i in a:
#     add=add+i
# print(add) 
  
 
for i in range(5):
     print("number is: "+str(i)+" and cube of the "+str(i)+" is: "+str(i*i*i))
        
    