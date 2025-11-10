def computepay(hours,rate):
    if hours>40:
        reg = 40*rate
        otp = (hours-40)*(rate*1.5)
        pay = reg + otp
    else:
        pay = hours * rate
    return pay
sh = input("Enter hour: ")
sr = input("Enter rate: ")
fh = float(sh)
fr = float(sr)
pay = computepay(fh,fr)
print(f"Pay {pay:.2f}")        