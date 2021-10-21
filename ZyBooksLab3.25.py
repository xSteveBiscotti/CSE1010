sqft_per=200.0
labor_hour=40.0
exorcism=100.0

# define the function
def cost():
    paint = (sqft_painted / sqft_per)
    laborhr = ((sqft_painted / sqft_per) * 10)
    paintcost = (ppg * paint)
    laborcost = (laborhr * labor_hour)
    echarge = (demons * exorcism)
    total_cost = (echarge + paintcost + laborcost)
    outputtuple = (paint, laborhr, paintcost, laborcost, echarge, total_cost)
    print(outputtuple)
    
# ask for input
sqft_painted=float(input("How many sqft is required to be painted?"))
print('')
ppg=float(input("What is the paint price per gallon?"))
print('')
demons=float(input("How many demons need to be exorcised?"))
print('')

# call the function and print
cost()