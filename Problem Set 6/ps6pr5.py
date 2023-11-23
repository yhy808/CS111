#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# TT Securities    
#
# Computer Science 111
#

import math

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.
def avg_price(prices):
    """ returns the average price.
        input: prices is a list of 1 or more numbers.
    """
    result = 0
    for i in range(len(prices)):
        result += prices[i]
    result /= len(prices)
    return result

def std_dev(prices):
    """ returns the standard deviation of the prices.
        input: prices is a list of 1 or more numbers.
    """
    result = 0
    for i in range(len(prices)):
        result += (prices[i] - avg_price(prices)) ** 2
    result /= len(prices)
    result **= 0.5
    return result
    
def max_day(prices):
    """ returns the day of the maximum price.
        input: prices is a list of 1 or more numbers.
    """
    m = prices[0]
    result = 0
    for i in range(len(prices)):
        if prices[i] > m:
            m = prices[i]
            result = i
    return result

def any_lower(prices, n):
    """  return True if there are any prices below the threshold, and False otherwise """
    for i in prices:
        if i < n:
            return True
    return False
         
def find_tts(prices):
    """ find the best days on which to buy and sell the stock.
        input: a list of 2 or more prices.
    """
    maxdiff = prices[1] - prices[0]
    m = 0
    n = 1
    for x in range(len(prices)):
        for y in range(len(prices))[x + 1:]:
            d = prices[y] - prices[x]
            if d > maxdiff:
                maxdiff = d
                m = x
                n = y
    return [m] + [n] + [maxdiff]
    

def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            avg = avg_price(prices)
            print('The average price is', avg)
        elif choice == 4:
            std = std_dev(prices)
            print('The standard deviation is', std)
        elif choice == 5:
            max_d = max_day(prices)
            print('The max price is', prices[max_d], "on", max_d)
        elif choice == 6:
            n = int(input('Enter the threshold:'))
            if any_lower(prices, n) == True:
                print('There is at least one price below', n)
            else:
                print('There are no prices below', n)
        elif choice == 7:
            buy_day = find_tts(prices)[0]
            sell_day = find_tts(prices)[1]
            diff = find_tts(prices)[2]
            print('Buy on day', buy_day, 'at price', prices[buy_day])
            print('Sell on day', sell_day, 'at price', prices[sell_day])
            print('Total profit:', diff)
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
