# Kaprekar's Constant (6174) Routine with Unit Testing

This repository contains a Python program to process the Kaprekar's constant (6174) routine using a four-digit number. The program performs the following steps:

1. Takes a four-digit number as input (with at least two different digits, excluding 1111 and 0000).
2. Arranges the digits in descending and ascending order to form two four-digit numbers, adding leading zeros if needed.
3. Subtracts the smaller number from the larger number.
4. Repeats the process until the result is 6174 (Kaprekar's constant).

The project also includes **Unit Tests** written using the `unittest` framework to ensure the correctness of the program.

## Routine Example:
For input `9218`, the steps are as follows:
- 9218 → 9821 (descending), 1289 (ascending)
- 9821 - 1289 = 8532
- 8532 → 8532 (descending), 2358 (ascending)
- 8532 - 2358 = 6174 (Kaprekar's constant)

## Unit Testing
The program includes 10 test cases that verify the correctness of the routine using various inputs. The tests use different assert methods to check the correctness of the computed results.

## Requirements
- Python 3.x
- `unittest` module (included in Python standard library)

## How to Run:
1. Clone the repository.
2. Run the program to process the Kaprekar's constant routine.
3. Run the test cases using the following command:
   ```bash
   python -m unittest test_file.py
