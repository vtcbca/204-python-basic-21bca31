#pallindrome string or not
string=input(("enter a string: "))
if(string==string[::-1]):
    print("the string is a pallindrome")
else:
    print("not a pallindrome")
