ph = int(input('Enter your pH number between 0 and 14: '))

if ph > 7:
    print ('Basic')
elif ph < 7:
    print('Acidic')
else:
    print('Neutral')