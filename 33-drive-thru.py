menu = ['🍔 Cheeseburger',
        '🍟 Fries',
        '🥤 Soda',
        '🍦 Ice Cream',
        '🍪 Cookie']

def get_item(x):
    return menu[x-1]

def welcome():
    print("Welcome to McDonald's! Please, select one item from the menu:")
    for i in range(len(menu)):
        print(menu[i])

welcome()
order = int(input('\nEnter your order: '))
print(get_item(order))