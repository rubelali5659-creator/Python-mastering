sh = input("Enter hour: ")
sr = input("Enter rate: ")
xh = float(sh)
xr = float(sr)
if xh>40:
    # print("Overtime")
    reg = xr*40
    otp = (xh-40)*(xr*10.5)
    # print(reg,otp)
    xp = reg+otp
    print(f"Pay:{xp:.2f}")
else:
    # print("Regular")
    xp = xh*xr
    print(f"Pay:{xp:.2f}")
