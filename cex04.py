def recalling1(x,y):
    if x>40:
        reg = 40*y
        otp = (x-40)*(y*1.5)
        z = reg + otp
    else:
        z = x*y
    #print("Returning",z)
    return z
a = input("Enter hour: ")
b = input("Enter rate: ")
ax = float(a)
by = float(b)
z = recalling1(ax,by)
print(f"Pay {z:.2f}")