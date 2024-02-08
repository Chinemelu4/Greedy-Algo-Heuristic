#!/usr/bin/env python
import click

def greedy_coin(change):
    """Return a dictionary of the coin type as a key and the number of coins as the value"""

    print(f"your change for {change} is: ")

    coins = [0.25, 0.10, 0.05, 0.01] 
    coin_lookup = {0.25:'quarter', 0.10:'dime', 0.05: 'nickel',0.01:'penny'}
    coin_dict = {}
    for coin in coins:
        coin_dict[coin]=0
    for coin in coins:
        while change >= coin:
            change -= coin
            coin_dict[coin] += 1
    for coin in coin_dict:
        if coin_dict[coin] > 0:
            print(f"{coin_dict[coin]} {coin_lookup[coin]}")
    return coin_dict


@click.command()
@click.argument("change",type=float)
def main(change):
    """
    Return the minimum number of coins for a given change

    Example: ./change_dispenser.py 0.89
    """

    greedy_coin(change)

if __name__ =="__main__":
    main()