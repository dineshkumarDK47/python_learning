#---> tuple <--- symbol - ()
# Advantages ot tuper over list :
#     allows duplicate
#     tuple - heterogeneous 
#     list - homogeneous
#     ant type can be acceptable
#     tuple is immutable (cannot modify)
#     can be used in dictionary as KeyboardInterrupt
    
tuple = (1,2,3,"dk",[1,2,3])
print(tuple)
print(tuple[0])
print(tuple[-4])

#in tuple no add or remove

#tuple methods :
my_tuple = (3,7,7,4,3)
print(my_tuple.count(7))

for t in my_tuple:
    print(t,end=" ")

