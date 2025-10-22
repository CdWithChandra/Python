

dobj={0:"ZERO",1: "ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
dig=int(input("Enter any digit: "))
res=dobj.get(dig) if dobj.get(dig)!=None else "+ve number" if dig>0 \
    else "-ve digits" if dig<0 and dig in [-1,-2,-3,-4,-5,-6,-7,-8,-9] else "-ve number"
print("{} is {}".format(dig,res))