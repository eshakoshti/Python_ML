str="hello"
print(str)

no={11,22,33,44,55,66}
print(no)
no.remove(66)
print(no)
print("After Removing Data:",no)
print("Convert Frozenset:",frozenset(no))

str1="python program"
s1="portable"
upper_str=str1[:6].upper()
print("After convert:",upper_str)
print("Concating string:",str1,s1)

str2="mississpi"
i=2
print(str2.index('p'))
print("Count no of string:",str2.count('i'))
print("Reverse using slicing:",str2[::-1])
print("Upper letter two letter:",str2[:2].upper()+str2[3:])
print("index",str2[i])
print("Replace  all i with t ",str2.replace('i','t'))
print("string Length:",len(str2))





