numbers ="1","2","3",
letters= "a","b","c",
print (numbers [0])
print (letters[-1])
new_tuple = numbers+letters
print (new_tuple)
result_len = len(new_tuple)
print (result_len)
if "4" in new_tuple :
    print ("4 in the result_len ")
else : print( "4 not in the result_len") 
list1 = [4,5,6]
new_tuple2= tuple(list1)
var1,var2,var3 = numbers
var4,var5 ,var6 = letters
e_tuple = enumerate(letters[1])
print(tuple(e_tuple))
count_numbers= numbers.count("2",)
print (count_numbers)
new_tuple3 = enumerate (new_tuple)
print (tuple(new_tuple3))