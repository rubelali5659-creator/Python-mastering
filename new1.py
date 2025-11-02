# this code allows my till learning full potential
# input part for Rubel:
xr = input("Enter Rubel's rate: ")
xh = input("Enter Rubel's hour: ")
xp = float(xr)*float(xh)
# input for Taslim:
yr = input("Enter Taslim's rate: ")
yh = input("Enter Taslim's hour: ")
yp = float(yr)*float(yh)
# input for Rasel:
zr = input("Enter Rasel's rate: ")
zh = input("Enter Rasel's hour: ")
zp = float(zr)*float(zh)
# total payment for each:
print (f"Rubel Earned {xp:.2f}")
print (f"Taslim Earned {yp:.2f}")
print (f"Rasel Earned {zp:.2f}")
# condition part:
if xp>yp and xp>zp:
    print("Rubel earns more")
elif yp>xp and yp>zp:
    print("Taslim earns more")
elif zp>xp and zp>yp:
    print("Rasel earns more")
else:
    print("Everyone's earning is same")

