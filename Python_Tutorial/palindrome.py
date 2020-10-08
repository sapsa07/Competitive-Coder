# Using reverse()
str1 = input("Enter String :")
lst1 = list(str1)
lst2 = lst1.copy()
lst2.reverse()

if lst1 == lst2 :
    print("Palindrome")
else :
    print("Not")