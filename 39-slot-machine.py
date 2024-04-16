import random

symbols = ['🍒',' 🍇', '🍉', '7️⃣']
results = []

def play():
    answer = ''
    while answer != 'N':
        results.clear()
        for _ in range(3):
            results.append(random.choice(symbols))
        print(results[0], ' | ', results[1], ' | ', results[2])

        if all(symbol == symbols[3] for symbol in results):
            print('Jackpot! 💰')
        else:
            print('Thanks for playing!')

        print('Do you want to play again?')
        print("Press 'Y' for yes or 'N' for no.")
        answer = input().upper()

play()
