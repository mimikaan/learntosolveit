
f = int(input("Enter free sizes remain in flopy :"))
u = int(input("Amount of used memory : "))
total = f+u
o = int(input("Deleted file size :"))
if o <= u:
    u = u-o
    f = f+o
else:
    print("can't be deleted more then used memory")
n = int(input("Enter the new file size :"))
if n <= f:
    f = f-n
    u = u+n
else:
    print("Can't be created more then available memory")
print("The free size remains is {}".format(f))
