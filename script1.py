#was to print message
#a=input("Enter Name:")
#def msg():
#    print("Good Morning ()".format (a));
#msg()
#function without argument


#function with argument
a=input("Enter any Name:")
def msg(x):
    print("Good Morning"+x)
    msg(a)
