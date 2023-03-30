# Difference between == and === :-
# == operator checks whether the value is equal or not, i.e it checks the equality of the values.
# === operator check the identity of the two values i.e checks the data type of the values.


string = "Mayank"
for i in string:
    if i == "a" :
        pass                # This will do nothing as this is a null operation(placeholder).
    elif i == "n":
        print("n will get skipped")
        continue                         # This will skip 'a' and will return back to the loop.
    print(i)


#Program on Break Statement

for i in range(5) : 
    if(i == 3) : 
        break
    i += 1                        # It will break the loop when 'i' will be equal to 3.
    print(i)

    

# program by using range() with three parameter start, stop and step-size

for j in range (2,30,4):
    print(j)     

# This will print all the numbers between 2 
#and 30 with a setp size of 4, i.e this will print
# 2
# 6
# 10
# 14
# 18
# 22
# 26 