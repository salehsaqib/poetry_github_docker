tot_amt:int = int(input("Enter amount: "))
perc:int = int(input("Enter Percentage to calculate: "))
answer:int =  int(tot_amt * perc/100)
print(f"{perc}% of {tot_amt} is :{answer}")
