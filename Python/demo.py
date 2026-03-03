str="welcome"
print(str)
print("|".join(str))


no={11,22,33,44,55,66}
print(no)
no.remove(66)
print(no)
print("After Removing Data:",no)
print("Convert Frozenset:",frozenset(no))

# ===========Type Casting intger to float=============
data=(3)
d=float(3.0)
print("Type Casting:",d)


str1="python program "
s1="portable"
upper_str=str1[:6].upper()
print("After convert:",upper_str)
print("Concating string:",str1,s1)

#==========Present string  in or not==========
txt="welcome to my healthcare website"
print("Present in string:","healthcare" in txt)
print("Not present string:","good" not in txt)
print("Present string:","good"  in txt)


str2="mississpi"
i=2
print("Index of No:",str2.index('p'))
print("Count no of string:",str2.count('i'))
print("Reverse using slicing:",str2[::-1])
print("Upper letter two letter:",str2[:2].upper()+str2[3:])
print("index",str2[i])
print("Replace  all i with t ",str2.replace('i','t'))
print("string Length:",len(str2))





