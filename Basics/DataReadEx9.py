#program for calculating simple interest

p=float(input("Enter princial amount: "))
t=float(input("Enter time:"))
r=float(input("Enter rate of interest:"))

#calculate simple interest and tot amount to pay
si=(p*t*r)/100
totamt=p=si
print("Simple interest calculations")
print("-"*25,"or","-"*25)
print("Principal amount: {}".format(p))
print("Time: {}".format(t))
print("Rate of Interest:{}".format(r))
print("Simple Interest={}".format(si))
print("Total Amount to pay={}".format(totamt))