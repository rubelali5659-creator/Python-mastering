rx = input("Enter a number: ")
try:
    px = int(rx)
except:
    px = -1
if px>0:
    print("Number")
else:
    print("Not a number")
