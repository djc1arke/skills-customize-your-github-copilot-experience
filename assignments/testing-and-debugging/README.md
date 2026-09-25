# 📘 Assignment: Testing and Debugging Python Programs

## 🎯 Objective

Learn how to use `pytest` to check Python functions, interpret failing test results, and debug a program until it behaves correctly.

## 📝 Tasks

### 🛠️ Write Tests for the Order Helpers

#### Description
Create a file named `test_starter_code.py` and write tests for the functions in `starter-code.py`. Test normal inputs as well as important boundary cases, such as an empty order and an invalid quantity.

#### Requirements
Completed program should:

- Include at least two tests for `calculate_total()`
- Include at least two tests for `has_stock()`
- Include at least two tests for `average_rating()`
- Use clear test names that describe the behavior being checked
- Include at least one boundary or invalid-input test

### 🛠️ Run Tests and Diagnose Failures

#### Description
Run your test suite with `pytest`. Read each failure message, identify whether the problem is in your test or in `starter-code.py`, and record the cause of each bug in a short comment or a separate notes file.

#### Requirements
Completed program should:

- Run the tests with the `pytest` command
- Use the failure output to locate the incorrect behavior
- Explain the cause of each failing behavior before changing the code

### 🛠️ Fix the Functions

#### Description
Correct the bugs in `starter-code.py` without changing the function names or parameters. Run the full test suite again after each meaningful fix.

#### Requirements
Completed program should:

- Calculate an order total using each item's price and quantity
- Return `True` from `has_stock()` only when the requested quantity is available
- Return the correct average for a list of ratings
- Handle an empty ratings list without crashing
- Pass all of your tests with no failures
