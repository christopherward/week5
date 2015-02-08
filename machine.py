#Christopher Ward
#MPCS 50101, Homework 5
class CoinDispenser:
    # initialize list of coin values
    coins = [25, 10, 5, 1]

    def make_change(self, amount):
        # use integer division to determine number of coins needed
        quarters = amount // 25
        dimes = (amount - 25 * quarters) // 10
        nickels = (amount - (25 * quarters + 10 * dimes)) // 5
        pennies = (amount - (25 * quarters + 10 * dimes + 5 * nickels))

        # return number of quarters, dimes, nickels, and pennies
        return [quarters, dimes, nickels, pennies]
