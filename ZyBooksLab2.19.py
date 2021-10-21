#Get values from customer
lemonJuice = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agaveNectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))

print('')
print('Lemonade ingredients - yields ' + '{:.2f}'.format(servings) + ' servings')
print('{:.2f}'.format(lemonJuice) + ' cup(s) lemon juice')
print('{:.2f}'.format(water) + ' cup(s) water')
print('{:.2f}'.format(agaveNectar) + ' cup(s) agave nectar')
print('')

servingsDesired = float(input('How many servings would you like to make?\n'))
print('')

newLemon = (servingsDesired / 3)
newWater = (servingsDesired * 2.6666 )
newAgave = (servingsDesired / 2.4 )

print('Lemonade ingredients - yields ' + '{:.2f}'.format(servingsDesired) + 'servings')
print('{:.2f}'.format(newLemon) + ' cup(s) of lemon juice')
print('{:.2f}'.format(newWater) + ' cup(s) of water')
print('{:.2f}'.format(newAgave) + ' cup(s) of agave nectar')
print('')

galLemon = (newLemon / 16)
galWater = (newWater / 16)
galAgave = (newAgave / 16)

print('Lemonade ingredients - yields ' + '{:.2f}'.format(servings) + 'servings')
print('{:.2f}'.format(galLemon) + ' gallon(s) of lemon juice')
print('{:.2f}'.format(galWater) + ' gallon(s) of water')
print('{:.2f}'.format(galAgave) + ' gallon(s) of agave nectar')
