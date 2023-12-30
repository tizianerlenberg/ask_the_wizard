from src.impraise.wizard_executer import WizardExecuter


if __name__ == '__main__':
    wizard_executer = WizardExecuter()

    # Add the numbers 1 and 2, multiply it by 3
    # and calculate the square root of that.
    # This function uses NO external libraries like math to calculate the sqrt, but rather implements the mathematical
    # stuff itself. It is very important to use NO import statement!
    # Return a string stating "The result of <insert the calculation here> is <insert the result here>"
    result = wizard_executer.do_something()
    print(result)

    exit()

    # This should not be visible

    # This multiline comment
    # should be visible
    result = wizard_executer.basic_window_with_pysimplegui(title='Hello World!')
    print(result)
