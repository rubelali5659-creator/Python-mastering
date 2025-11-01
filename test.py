# this is a test code (Rubel Part)
xr = input("Enter Rubel's rate: ")
xh = input("Enter Rubel's hour: ")
x = float(xr)*float(xh)
# This Taslim Part
yr = input("Enter Taslim's rate: ")
yh = input("Enter Taslim's hour: ")
y = float(yr)*float(yh)
# this is total payent part
print(f"Rubel earned: {x:.2f}")
print(f"Taslim earned: {y:.2f}")
#this is condition part
if x>y:
    print('Rubel earns more')
elif x<y:
    print('Taslim earns more')
else:
    print('Both earns same!')