#Python program to calculate simple interest
p=float(input("Enter principal amount: "))
r=float(input("Enter rate of interest: "))
t=float(input("Enter time period: "))
si=(p*t*r)/100
totamt=p+si
print("---------Perticulars----------")
print("Principal Amount={}".format(p))
print("Rate of interest={}".format(r))
print("Time period={}".format(t))
print("Simple interest={}".format(si))
print("Total amount={}".format(totamt))

