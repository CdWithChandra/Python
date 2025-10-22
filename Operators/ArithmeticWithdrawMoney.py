#Python program to withdraw money 500, 200 and 100 from ATM
amount=int(input("Enetr how much you want to withdraw: ")) #9300
oamt=amount
#How many 500 notes
no500=amount//500
#Remaining amount after 500s
amount=amount%500
#How many 200 notes
no200=amount//200
#Remaining amount after 200s
amount=amount%200
#How many 200 notes
no100=amount//100
#Remaining amount after 200s
amount=amount%100
print("------------------------")
print("Money Available: {}".format(oamt))
print("No of 500s: {}".format(no500))
print("No of 200s: {}".format(no200))
print("No of 100s: {}".format(no100))

9014144952

