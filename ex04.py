def computepay(hours, rate):
    print("In computepay", hours, rate)
    sh = input("Enter hour: ")
    sr = input("Enter rate: ")
    xh = float(sh)
    xr = float(sr)
    computepay(xh,xr)
    if xh>40:
        #print("Overtime")
        reg = 40*xr
        otp = (xh-40)*(xr*1.5)
        xp = reg + otp
    else:
        #print("Regular")
        xp = xh*xr
    print(f"Pay:{xp:.2f}")
