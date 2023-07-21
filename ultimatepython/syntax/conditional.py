"""
This module shows how to use if blocks, if-else blocks and if-elif-else
blocks to decide which lines of code to run (and skip).
"""


def main():
    x_add_two = 1 + 2
    ran_1 = x_add_two == 3
    assert ran_1

    ran_2 = x_add_two != 1
    assert ran_2

    # There are `else` statements as well, which run if the initial condition
    # fails. Notice that one line gets skipped and this conditional does not
    # help us make a conclusion on the variable's true value
    ran_3 = x_add_two != 1
    assert ran_3

    # The `else` statement also runs once all other `if` and `elif` conditions
    # fail. Notice that multiple lines get skipped, and that all of the
    # conditions could have been compressed to `x_add_two != 3` for
    # simplicity. In this case, less logic results in more clarity
    ran_4 = x_add_two != 1 and x_add_two != 2 and x_add_two >= 3 and x_add_two <= 3
    assert ran_4


if __name__ == "__main__":
    main()
