#Christopher Ward
#MPCS 50101, Homework 5
class CoinDispenser:
    coins = [25, 10, 5, 1]

    def make_change(self, amount):
        quarters = amount // 25
        dimes = (amount - 25 * quarters) // 10
        nickels = (amount - (25 * quarters + 10 * dimes)) // 5
        pennies = (amount - (25 * quarters + 10 * dimes + 5 * nickels))
        return [quarters, dimes, nickels, pennies]
