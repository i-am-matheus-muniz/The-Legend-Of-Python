height = int(input('Enter your height: '))
credits = int(input('Enter your available credits: '))

if height >= 137 and credits >= 10:
    print('Enjoy the ride!')
elif height < 137 and credits >= 10:
    print('You are not tall enough to ride.')
elif height >= 137 and credits < 10:
    print('You do not have enough credits.')
else:
    print('You do not met either requirements.')