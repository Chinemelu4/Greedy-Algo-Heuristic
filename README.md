# Greedy Coin Dispenser

This Python script provides a simple command-line interface for determining the minimum number of coins needed to represent a given amount of change. It utilizes a greedy algorithm to dispense coins in the most efficient way possible.

## Usage

To use the script, follow these steps:

1. Make sure you have Python installed on your machine.
2. Clone this repository to your local machine or download the script directly.
3. Open a terminal or command prompt in the directory where the script is located.

Run the script with the following command:

```bash
./change_dispenser.py <change_amount>
```

Replace `<change_amount>` with the desired amount of change for which you want to calculate the minimum coins. The script will then display the optimal combination of coins to make up the given change.

## Example

```bash
./change_dispenser.py 0.89
```

Output:

```
your change for 0.89 is:
3 quarter
1 dime
1 nickel
4 penny
```

In this example, the script returns the minimum number of coins needed to represent $0.89, which includes 3 quarters, 1 dime, 1 nickel, and 4 pennies.

Feel free to experiment with different change amounts and observe the efficient coin dispensing provided by the script.